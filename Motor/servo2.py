from gpiozero import Servo
from time import sleep

servo=Servo(18)

while True:
    servo.min()
    print('min')
    sleep(1)
    servo.mid()
    print('mid')
    sleep(1)
    servo.max()
    print('max')
    sleep(1)
    servo.mid()
    print('mid')
    sleep(1)