import os
from dotenv import load_dotenv

# Cargar variables de entorno desde un archivo .env
load_dotenv()

# Configuración General
DEBUG = True
SECRET_KEY = os.getenv('SECRET_KEY', 'aca91uJfpaRE2ef6XXr3hJ6JwxsanEMHI61EbUPW_SCiFZJ7tAA')

# Configuración de Base de Datos
DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': os.getenv('DB_NAME', 'db.sqlite3'),
        'USER': os.getenv('DB_USER', ''),
        'PASSWORD': os.getenv('DB_PASSWORD', ''),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}

# Configuración de Redes
WIFI_SSID = os.getenv('WIFI_SSID', 'default_ssid')
WIFI_PASSWORD = os.getenv('WIFI_PASSWORD', 'default_password')

# Configuración de BLE (Bluetooth Low Energy)
BLE_SCAN_INTERVAL = int(os.getenv('BLE_SCAN_INTERVAL', '10'))  # Intervalo en segundos

# Otras Configuraciones
LOGGING_LEVEL = os.getenv('LOGGING_LEVEL', 'DEBUG')
