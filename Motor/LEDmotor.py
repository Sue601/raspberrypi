from gpiozero import Motor
from gpiozero import LED
import time

motor = Motor(forward=17, backward=27)
led=LED(20)

while True:
    print('Forward')
    motor.forward(speed=0.5)
    led.on()
    time.sleep(5)
    
    print('backward')
    motor.backward(speed=0.1)
    led.off()
    time.sleep(5)


