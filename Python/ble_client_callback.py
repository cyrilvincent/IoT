import asyncio
import time
from bleak import BleakClient

address = "3C:8A:1F:D3:D7:02"
sensor_uuid = "19b10001-e8f2-537e-4f6c-d104768a1214"
led_uuid = "19b10002-e8f2-537e-4f6c-d104768a1214"

def callback(sender, data: bytearray):
    print(f"Received: {data.decode()}")

async def main(address):
    async with BleakClient(address) as client:
        print(client)
        print(f"Connected: {client.is_connected}")
        for service in client.services:
            print(service)
        await client.start_notify(sensor_uuid, callback)        
        led_value = 0
        for i in range(100):
            led_value = 0 if led_value == 1 else 1
            print("Led: " + str(led_value))
            await client.write_gatt_char(led_uuid, str(led_value).encode(), response=True)
            time.sleep(0.7) 
        


asyncio.run(main(address))

