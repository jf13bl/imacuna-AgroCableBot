import paho.mqtt.client as mqtt
from django.conf import settings
import json
import os
from dotenv import load_dotenv

load_dotenv()

def on_connect(mqtt_client, userdata, flags, rc):
    if rc == 0:
        print('Connected successfully')
        mqtt_client.subscribe('sensores')
        mqtt_client.subscribe('comandos')
    else:
        print('Bad connection. Code:', rc)

    
def on_message(client, userdata, msg):
    from .models import Sensor_MQTT 
    try:
        data = json.loads(msg.payload.decode('utf-8'))
        Sensor_MQTT.objects.create(
            acelerometro_roll=data['acelerometro']['roll'],
            acelerometro_pitch=data['acelerometro']['pitch'],
            acelerometro_yaw=data['acelerometro']['yaw'],
            giroscopio_roll=data['giroscopio']['roll'],
            giroscopio_pitch=data['giroscopio']['pitch'],
            giroscopio_yaw=data['giroscopio']['yaw'],
            magnetometro_x=data['magnetometro']['x'],
            magnetometro_y=data['magnetometro']['y'],
            magnetometro_z=data['magnetometro']['z'],
            orientacion_roll=data['orientacion']['roll'],
            orientacion_pitch=data['orientacion']['pitch'],
            orientacion_yaw=data['orientacion']['yaw'],
            humedad=data['humedad']['value'],
            presion=data['presion']['value'],
            temperatura=data['temperatura']['value']
        )
    except Exception as e:
        print("Error al procesar y guardar los datos:", e)


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(os.environ['MQTT_USER'], os.environ['MQTT_PASSWORD'])

try:
    # Intentar conectar al servidor MQTT
    client.connect(
        host=os.environ['MQTT_SERVER'],
        port=int(os.environ['MQTT_PORT']),
        keepalive=int(os.environ['MQTT_KEEPALIVE']),
    )
    # Comenzar el bucle de escucha de MQTT
    client.loop_start()
except Exception as e:
    print("No se pudo conectar al servidor MQTT:", e)



