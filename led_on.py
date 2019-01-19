import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)

GPIO_OUT = 4

try:
  while True:
    GPIO.output(GPIO_OUT, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(GPIO_OUT, GPIO.LOW)
    time.sleep(1)

except KeyboardInterrupt:
  GPIO.cleanup()