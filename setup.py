from setuptools import setup, find_packages

setup(
    name='OpenAI_Catalina',
    version='0.1',
    description='Proyecto para control de dispositivos y conectividad de red.',
    author='Oscar',
    author_email='repuestosrecicla2@gmail.com',  # Actualiza con tu correo
    packages=find_packages(where='modules'),  # Asumiendo que los paquetes están en /modules
    install_requires=[
        'requests==2.28.2',
        'numpy==1.23.4',
        'scapy==2.4.5',
        'python-dotenv==1.0.0',
        'bleak==0.19.1',
    ],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            # Agrega aquí cualquier comando de consola si es necesario
            # 'nombre_comando=modulo:funcion',
        ],
    },
)
