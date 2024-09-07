from scapy.all import *
import logging

# Configuración del logging
logging.basicConfig(level=logging.DEBUG)  # Puedes ajustar el nivel de logging según tus necesidades
logger = logging.getLogger(__name__)

def scan_network(ip_range):
    logger.info(f"Escaneando dispositivos en la red {ip_range}")

    # Generar paquetes ARP
    arp_request = ARP(pdst=ip_range)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request

    # Enviar paquetes y recibir respuestas
    answered_list = srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    # Lista de dispositivos encontrados
    devices = []
    for element in answered_list:
        devices.append({'ip': element[1].psrc, 'mac': element[1].hwsrc})

    return devices

if __name__ == "__main__":
    target_network = "192.168.1.0/24"
    logger.info("Iniciando escaneo de redes Wi-Fi")
    networks = scan_network(target_network)
    
    # Mostrar redes encontradas
    logger.info("Redes Wi-Fi encontradas:")
    for network in networks:
        logger.info(f"IP: {network['ip']}, MAC: {network['mac']}")

