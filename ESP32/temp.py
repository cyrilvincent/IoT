import time
import machine
import math

print("Temperature")
p2 = machine.Pin(2, machine.Pin.OUT)
p4 = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_DOWN)
adc = machine.ADC(15) # Mettre une resistance 22KOhm
B = 4275;
C = 2.7
R0 = 100000;

while True:
    value = p4.value()
    if value == 1:
        p2.on()
    else:
        p2.off()
    val16 = adc.read_u16()
    valv = adc.read_uv()
    R = 65536.0/val16-1.0;
    R *= R0 * C
    print(val16, R, R0)
    temp = 1.0/(math.log(R/R0)/B+1/298.15)-273.15;
    print(f"Value16: {val16} ValueMilliVolt: {valv // 1000} Temp: {temp:.1f}")
    time.sleep_ms(1000)