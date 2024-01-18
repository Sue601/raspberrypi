from gpiozero import PWMLED        
from time import sleep            
 
pwmled = PWMLED(4)                    
brightrange=[x*0.01 for x in range(0,100)]         

while True:
     for brightness in brightrange:           
          pwmled.value=brightness             
          print(led.value)                  
          sleep(0.05)                       

     for brightness in reversed(brightrange):    
          pwmled.value=brightness              
          print(led.value)                     
          sleep(0.05)             


