import time
import machine
import math

print("Sensor & Buzzer")
p2 = machine.Pin(2, machine.Pin.OUT)
p5 = machine.Pin(5, machine.Pin.OUT)
p18 = machine.Pin(18, machine.Pin.IN)

while True:
    value = p18.value()
    print(value)
    if value == 1:
        p2.on()
        p5.on()
        p5.off()
    else:
        p2.off()
        p5.off()
    time.sleep_ms(100)
