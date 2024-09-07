class RelayController:
    def __init__(self, ip_address):
        self.ip_address = ip_address
    
    def turn_on(self, relay_id):
        print(f"Encendiendo relé {relay_id} en {self.ip_address}")
        # Aquí iría el código para encender el relé
    
    def turn_off(self, relay_id):
        print(f"Apagando relé {relay_id} en {self.ip_address}")
        # Aquí iría el código para apagar el relé
