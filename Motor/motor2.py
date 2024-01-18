from gpiozero import Robot
import time

dc_motor = Robot(left=(17,27),right=(20,21))

for num in range(4):
    print(num,"Forward")
    dc_motor.forward(speed=1)
    time.sleep(3)
    
    print("stop")
    dc_motor.stop()
    time.sleep(5)
    
    print(num,"backward")
    dc_motor.backward(speed=0.3)
    time.sleep(3)

dc_motor.stop()

