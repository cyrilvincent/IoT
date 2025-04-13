import time
import machine
import bme280_float as bme280

print("BME280")
i2c = machine.SoftI2C(sda=machine.Pin(21), scl=machine.Pin(22))
bme = bme280.BME280(i2c=i2c)

while True:
    print(bme.values)
    time.sleep_ms(1000)
    