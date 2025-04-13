import time
import machine

print("Button")
p2 = machine.Pin(2, machine.Pin.OUT)
p4 = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    value = p4.value()
    print(value)
    if value == 1:
        p2.on()
    else:
        p2.off()
    time.sleep_ms(100)