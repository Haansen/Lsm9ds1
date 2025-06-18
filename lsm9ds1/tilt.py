import time
import board
import busio
import adafruit_lsm9ds1
import paho.mqtt.client as mqtt
import math

MQTT_SERVER = "homeassistant.local"
MQTT_USER = "mqtt_user"
MQTT_PASS = "mqtt_password"

client = mqtt.Client()
client.username_pw_set(MQTT_USER, MQTT_PASS)
client.connect(MQTT_SERVER, 1883, 60)

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_lsm9ds1.LSM9DS1_I2C(i2c)

while True:
    try:
        x, y, z = sensor.acceleration
        tilt_x = math.degrees(math.atan2(x, z))
        tilt_y = math.degrees(math.atan2(y, z))

        client.publish("husvagn/tilt_x", round(tilt_x, 1))
        client.publish("husvagn/tilt_y", round(tilt_y, 1))

        time.sleep(5)
    except Exception as e:
        print("Error reading sensor or publishing:", e)
        time.sleep(5)
