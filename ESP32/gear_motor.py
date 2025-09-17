import time
import machine

print("Gear Motor")
motor = machine.Pin(6, machine.Pin.OUT)
button = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    value = button.value()
    print(value)
    if value == 1:
        motor.on()
    else:
        motor.off()
    time.sleep_ms(100)