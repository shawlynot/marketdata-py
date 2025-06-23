import json
from typing import AsyncGenerator
from websockets.asyncio.client import connect

async def subscribe_and_listen():
    websocket = await _subscribe()
    return _listen(websocket)
        
async def _subscribe():
    websocket = await connect("wss://ws.kraken.com/v2")
    await websocket.send(json.dumps({
        "method": "subscribe",
        "params": {
            "channel": "ohlc",
            "symbol": ["BTC/USD"]
        }
    }))
    message = await websocket.recv()
    print(message)
    return websocket

async def _listen(websocket) -> AsyncGenerator[list[dict]]:
    while True:
        received = await websocket.recv() # type: ignore
        data: dict = json.loads(received)
        if (data.get("channel") == "ohlc" and data.get("type") in ("update", "snapshot")):
            yield data["data"]