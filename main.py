import os
import logging
from settings import LOGGING_LEVEL
from wifisearchazukaki import scan_network  # Asegúrate de que esta importación sea correcta

# Definición de RelayController
class RelayController:
    def __init__(self, ip_address):
        self.ip_address = ip_address
    
    def turn_on(self, relay_id):
        print(f"Encendiendo relé {relay_id} en {self.ip_address}")
        # Aquí iría el código para encender el relé
    
    def turn_off(self, relay_id):
        print(f"Apagando relé {relay_id} en {self.ip_address}")
        # Aquí iría el código para apagar el relé

# Configuración del logging
logging.basicConfig(level=LOGGING_LEVEL)
logger = logging.getLogger(__name__)

def main():
    logger.info("Iniciando OpenAI Catalina")

    # Configuración del controlador de relé
    relay_ip = os.getenv('RELAY_IP', '192.168.1.100')  # Dirección IP del relé
    relay_controller = RelayController(relay_ip)

    # Ejemplo de encendido y apagado de relé
    relay_id = 1  # ID del relé que quieres controlar
    relay_controller.turn_on(relay_id)
    relay_controller.turn_off(relay_id)

    # Configuración del escáner Wi-Fi
    target_network = "192.168.1.0/24"
    logger.info("Iniciando escaneo de redes Wi-Fi")
    networks = scan_network(target_network)  # Usar la función directamente
    
    # Mostrar redes encontradas
    logger.info("Redes Wi-Fi encontradas:")
    for network in networks:
        logger.info(f"IP: {network['ip']}, MAC: {network['mac']}")

if __name__ == "__main__":
    main()

