import machine
import i2c_lcd
import time
import bme280_float as bme280

print("LCD Grove BME280 I2C")
i2c = machine.SoftI2C(sda=machine.Pin(21), scl=machine.Pin(22))
lcd = i2c_lcd.Display(i2c)
lcd.color(0,0,255)
lcd.home()
lcd.write("Starting BME    ")
bme = bme280.BME280(i2c=i2c)
lcd.write("Starting       ")
time.sleep_ms(1000)
lcd.color(255,255,255)

while True:
    temp, pre, hum = bme.read_compensated_data(result = None)
    lcd.home()
    lcd.write(f"Temperature:{temp}")
    lcd.move(0,1)
    lcd.write(f"Humidity:{hum:.1f}%")
    time.sleep_ms(1000)

