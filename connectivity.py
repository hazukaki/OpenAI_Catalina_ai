import bleak
import asyncio

async def discover_devices():
    # Ejemplo de código para descubrir dispositivos Bluetooth
    async with bleak.BleakScanner() as scanner:
        devices = await scanner.discover()
        for device in devices:
            print(f"Dispositivo encontrado: {device.name} - {device.address}")

async def main():
    try:
        await discover_devices()
    except bleak.BleakError as e:
        print(f"Error al descubrir dispositivos: {e}")

if __name__ == "__main__":
    asyncio.run(main())
