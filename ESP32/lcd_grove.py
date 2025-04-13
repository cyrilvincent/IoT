import i2c_lcd
import machine
import time

print("LCD Grove")
i2c = machine.SoftI2C(sda=machine.Pin(21), scl=machine.Pin(22))
d = i2c_lcd.Display(i2c)
d.home()
d.color(0,255,0)
d.write('Hello World')
time.sleep_ms(1000)
d.color(255,255,255)
i=0
while True:
    d.move(0,1)
    d.write(str(i))
    i+=1
    time.sleep_ms(1000)
    
