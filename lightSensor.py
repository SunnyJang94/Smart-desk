# 조도센서의 Interrupt를 감지하여 Interrupt발생시 조명 on/off를 제어하는 코드
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN)
GPIO.setup(10, GPIO.OUT)

def LIGHTON(gpio):
    GPIO.output(10, True)

booting = GPIO.input(26)
if booting == 1:
    GPIO.output(10, True)


GPIO.add_event_detect(26, GPIO.RISING, LIGHTON, 1000)
is_running = True
try:
    while is_running:
        time.sleep(2)

except KeyboardInterrupt:
    is_running = False
                
