from gpiozero import Motor
import time

motor = Motor(forward=17, backward=27)

while True:
    print('Forward')
    motor.forward(speed=0.5)
    time.sleep(5)
    
    print('backward')
    motor.backward(speed=0.1)
    time.sleep(5)

