import asyncio
from bleak import BleakScanner

# Se déconnecter de nRf connect
async def main():
    devices = await BleakScanner.discover()
    for d in devices:
        print(d)

asyncio.run(main())