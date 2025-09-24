import time
import machine
import math

print("Led Fading")
adc35 = machine.ADC(35, atten=machine.ADC.ATTN_11DB)
pwm2 = machine.PWM(machine.Pin(2), freq=1000, duty_u16=65535)

while True:
    val16 = adc35.read_u16()
    print(f"Value16: {val16}")
    pwm2.duty_u16(val16)
    time.sleep_ms(100)