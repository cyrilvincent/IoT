import machine
import i2c_lcd1602
import time
import bme280_float as bme280

print("LCD BME280 I2C")
i2c = machine.SoftI2C(sda=machine.Pin(21), scl=machine.Pin(22))
lcd = i2c_lcd1602.I2C_LCD1602(i2c)
lcd.puts("Starting BME")
bme = bme280.BME280(i2c=i2c)
lcd.puts("Starting    ")
time.sleep_ms(500)

while True:
    temp, pre, hum = bme.read_compensated_data(result = None)
    lcd.puts(f"Temperature:{temp}", 0, 0)
    lcd.puts(f"Humidity:{hum:.1f}%",0, 1)
    time.sleep_ms(1000)

