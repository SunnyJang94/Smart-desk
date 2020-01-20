import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

p_right = GPIO.PWM(18, 50)
p_left = GPIO.PWM(21, 50)
p_right.start(0)
p_left.start(0)

p_right.ChangeDutyCycle(6)
p_left.ChangeDutyCycle(3)
time.sleep(1)

