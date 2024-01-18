from gpiozero import Motor
import time

motor = Motor(forward=17, backward=27)

while True:
    print('Forward')
    motor.forward()
    time.sleep(5)
    
    print('backward')
    motor.backward()
    time.sleep(5)
