import adafruit_dht
import time
import digitalio
import board  

# Initialize the DHT11 sensor
dhtDevice = adafruit_dht.DHT11(4)  

while True:
    try:
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity
        print(f"Temperature: {temperature_c} °C  Humidity: {humidity}%")
        time.sleep(2)
    except RuntimeError as error:
        print(f"Runtime error: {error}")
        time.sleep(2)
    except Exception as error:
        dhtDevice.exit()
    

