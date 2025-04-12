#include <Wire.h>
#include "rgb_lcd.h"
#include "Seeed_BME280.h"

BME280 bme280;
rgb_lcd lcd;
String previous="";
String data="Waiting order";

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  lcd.begin(16, 2);
  lcd.setRGB(0, 0, 255);
  int i = bme280.init();
  lcd.print(data);
  delay(500);
  Serial.begin(9600);
  Serial.println(data);
}

void loop() {
  if(Serial.available() > 0) {
    digitalWrite(LED_BUILTIN, HIGH);
    lcd.setRGB(0,255,0);
    delay(100);
    previous = data;
    String input = Serial.readStringUntil('\n');
    if (input == "temp") {
      float temp = bme280.getTemperature();
      data = "Temperature:"+String(temp);
    }
    else if (input == "hum") {
      float hum = bme280.getHumidity();
      data = "Humidity:"+String(hum);
    }
    else if (input == "pre") {
      float pre = bme280.getPressure();
      data = "Pressure:"+String(pre);
    }
    else {
      data = "Unknow order:"+String(input);
    }
    Serial.println(data);
    data = data + "               ";
    delay(400);
    digitalWrite(LED_BUILTIN, LOW);
    lcd.setCursor(0, 0);
    lcd.print(previous);
    lcd.setCursor(0,1);
    lcd.print(data);
    lcd.setRGB(255, 255, 255); 
  }
}
