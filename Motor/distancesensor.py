from gpiozero import DistanceSensor
from gpiozero import Motor
import time

sensor=DistanceSensor(23,24) #echo=23,Trig=24
motor = Motor(forward=17, backward=27)
    
while True:
    if sensor.distance<=0.5:
        print('Distance to nearest object is',sensor.distance,'m','backward')
        motor.backward(speed=0.3)
        time.sleep(3)
        
    else:
        print('Distance to nearest object is',sensor.distance,'m','Forward')
        motor.forward(speed=0.5)
        time.sleep(3)
    
        




