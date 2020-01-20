# 적외선 리모콘의 신호에 따라 스마트책상의 기능을 제어하는 코드
# lirclight.py
# 모듈 선언
import RPi.GPIO as GPIO
import lirc
import time

# GPIO 선언부
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

# 좌우 서보모터 선언
p_right = GPIO.PWM(18, 50)
p_left = GPIO.PWM(21, 50)
p_right.start(0)
p_left.start(0)

ON = "on"
OFF = "off"
UP = "up"
DOWN = "down"

socketid = lirc.init("control", blocking=False)

# 4개의 적외선 리모콘 신호를 구분하여 수신시 해당 기능 실행 (조명 on/off, 서보모터 up/down)
while (True):
    codeIR = lirc.nextcode()
    if len(codeIR) !=0:
        print codeIR
        if codeIR[0] == ON:
            GPIO.output(10, True)
        elif codeIR[0] == OFF:
            GPIO.output(10, False)
        elif codeIR[0] == UP:
            p_right.ChangeDutyCycle(6)
            p_left.ChangeDutyCycle(3)
            time.sleep(1)
        elif codeIR[0] == DOWN:
            p_right.ChangeDutyCycle(3)
            p_left.ChangeDutyCycle(6) 
            time.sleep(1)

