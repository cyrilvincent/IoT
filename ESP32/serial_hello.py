import time
import machine

print("UART")
p2 = machine.Pin(2, machine.Pin.OUT) #Rx=16, Tx=17
uart = machine.UART(2, 9600)
time.sleep_ms(1000)

i=0
while True:
    p2.on()
    uart.write(f"Hello {i}\n")
    print(f"Hello {i}\n")
    i+=1
    time.sleep_ms(100)
    p2.off()
    time.sleep_ms(1000)