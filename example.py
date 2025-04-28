import asyncio
from bleak import BleakClient

bluetoothDeviceMac = ""
characteristicUuid = "00010203-0405-0607-0809-0a0b0c0d2b11"
packetData = "33050bf5aef4ffff000000000000000000000092"

async def send_packet():
    async with BleakClient(bluetoothDeviceMac) as device:
        await device.write_gatt_char(characteristicUuid, bytes.fromhex(packetData), response=False)

if __name__ == "__main__":
    asyncio.run(send_packet())

"""
3301000000000000000000000000000000000032 off
3301010000000000000000000000000000000033 on
3304240000000000000000000000000000000013 14% brightness
33050bf5aef4ffff000000000000000000000092 pink
"""
