import time
import machine
import math

print("Potentiometer")
adc = machine.ADC(35, atten=machine.ADC.ATTN_11DB)
# si on débrache le pin35 on voit bien les valeurs flottantes


while True:
    val16 = adc.read_u16()
    valv = adc.read_uv()
    ratio = val16 / 655.36
    print(f"Value16: {val16} ValueMilliVolt: {valv // 1000} Ratio: {ratio:.1f}")
    time.sleep_ms(100)