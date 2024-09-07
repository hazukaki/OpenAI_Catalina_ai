import os
import logging
import requests
from settings import WIFI_SSID, WIFI_PASSWORD, BLE_SCAN_INTERVAL, LOGGING_LEVEL

# Configuración del logging
logging.basicConfig(level=LOGGING_LEVEL)
logger = logging.getLogger(__name__)

class RelayController:
    def __init__(self, relay_ip):
        self.relay_ip = relay_ip
        self.base_url = f"http://{relay_ip}/api"

    def turn_on(self, relay_id):
        """Enciende el relé especificado por relay_id"""
        try:
            response = requests.post(f"{self.base_url}/relay/{relay_id}/on")
            response.raise_for_status()
            if response.status_code == 200:
                logger.info(f"Relé {relay_id} encendido correctamente.")
            else:
                logger.error(f"Error al encender el relé {relay_id}.")
        except requests.RequestException as e:
            logger.error(f"Error en la solicitud al encender el relé {relay_id}: {e}")

    def turn_off(self, relay_id):
        """Apaga el relé especificado por relay_id"""
        try:
            response = requests.post(f"{self.base_url}/relay/{relay_id}/off")
            response.raise_for_status()
            if response.status_code == 200:
                logger.info(f"Relé {relay_id} apagado correctamente.")
            else:
                logger.error(f"Error al apagar el relé {relay_id}.")
        except requests.RequestException as e:
            logger.error(f"Error en la solicitud al apagar el relé {relay_id}: {e}")

def main():
    relay_ip = os.getenv('RELAY_IP', '192.168.1.100')  # Dirección IP del relé, por defecto es 192.168.1.100
    controller = RelayController(relay_ip)

    # Ejemplo de uso
    relay_id = 1  # ID del relé que quieres controlar
    controller.turn_on(relay_id)
    controller.turn_off(relay_id)

if __name__ == "__main__":
    main()
