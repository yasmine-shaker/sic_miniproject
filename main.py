import binascii
import Adafruit_PN532 as PN532
import RPi.GPIO as GPIO
import time
from gpiozero import LED, Servo, Button

# --- Setup Raspberry Pi pins for SPI ---
CS   = 18
MOSI = 23
MISO = 24
SCLK = 25

# Create PN532 instance & led,servo,ldr setup
pn532 = PN532.PN532(cs=CS, sclk=SCLK, mosi=MOSI, miso=MISO)
GPIO.setup(LDR_PIN, GPIO.IN)
led = LED(LED_PIN)
servo = Servo(SERVO_PIN)

pn532.begin()

# Get firmware version (to check connection)
ic, ver, rev, support = pn532.get_firmware_version()
print("Found PN532 with firmware version: {0}.{1}".format(ver, rev))

# Configure to read MiFare cards
pn532.SAM_configuration()

print("Waiting for an NFC card...")

# --- Main Loop ---
while True:
   #card dedection
    uid = pn532.read_passive_target()
    if uid is not None:
        print("Card detected! UID: 0x{0}".format(binascii.hexlify(uid)))
        #ldr reading 
    if GPIO.input(LDR_PIN) == GPIO.LOW:  # night
        led.on()
        servo.min() 
        print("Night → LED ON, Servo at 90°")
    else:                                # morning
        led.off()
        servo.max()
        print("Day → LED OFF, Servo at 0°")
    time.sleep(1)
