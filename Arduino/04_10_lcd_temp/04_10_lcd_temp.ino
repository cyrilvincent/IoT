#include <Wire.h>
#include "rgb_lcd.h"
#include "Seeed_BME280.h"

rgb_lcd lcd;
BME280 bme280;

void setup() {
    pinMode(LED_BUILTIN, OUTPUT);
    Serial.begin(9600);
    Serial.println("Starting preasure BM280");
    lcd.begin(16, 2);
    lcd.setRGB(255, 0, 0);
    lcd.print("Starting");
    delay(1000);
    int i = bme280.init();
    lcd.setRGB(255, 255, 255);
}

void loop() {
    float temp = bme280.getTemperature();
    Serial.print("Temperature:"+String(temp));
    float hum = bme280.getHumidity();
    Serial.println(" Humidity:"+String(hum));
    lcd.setRGB((temp - 17) * 10, 32, 32);
    lcd.setCursor(0, 0);
    lcd.print("Temperature:"+String(temp));
    lcd.setCursor(0, 1);
    lcd.print("Humidity:"+String(int(hum))+"%");
    delay(200);
}

/*********************************************************************************************************
    END FILE
*********************************************************************************************************/