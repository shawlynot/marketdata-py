import asyncio
import marketdata.kraken

def main():
    asyncio.run(run())

async def run():
    ticks = await marketdata.kraken.subscribe_and_listen()
    async for tick in ticks:
        print(tick)

if __name__ == "__main__":
    main()
