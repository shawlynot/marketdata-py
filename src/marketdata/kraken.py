import asyncio
import json
from websockets.asyncio.client import connect

async def run():
    websocket = await subscribe()
    await listen(websocket)
        
async def subscribe():
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

async def listen(websocket):
    while True:
        message = await websocket.recv()
        print(message)

if __name__ == "__main__":
    asyncio.run(run())
