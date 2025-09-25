import time
import machine
import select
import sys
import i2c_lcd
import bme280_float as bme280

print("UART")
p2 = machine.Pin(2, machine.Pin.OUT)
uart = machine.UART(2, 9600)
i2c = machine.SoftI2C(sda=machine.Pin(21), scl=machine.Pin(22))
lcd = i2c_lcd.Display(i2c)
lcd.color(0,0,255)
lcd.home()
lcd.write("Starting BME    ")
bme = bme280.BME280(i2c=i2c)
uart.write(f"Starting\n")
lcd.write("Starting       ")
time.sleep_ms(1000)
lcd.color(255,255,255)

while True:
    if uart.any() > 0:
        time.sleep_ms(100)
        s = uart.readline().decode().strip()
        print(f"Receive {s}")
        lcd.move(0,0)
        lcd.write(s + "               ")
        temp, pre, hum = bme.read_compensated_data(result = None)
        print(f"Send {temp}")
        uart.write(f"Temp: {temp}\n")
        time.sleep_ms(100)