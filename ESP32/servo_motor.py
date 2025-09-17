from machine import Pin, PWM
from time import sleep
from servo import Servo

# Configure PWM on GPIO18
servo = Servo(18)

# Main loop
while True:
    servo.move(0)
    sleep(1)
    servo.move(180)
    sleep(1)
        


  

  


