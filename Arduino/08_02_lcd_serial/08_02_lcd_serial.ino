#include <Wire.h>
#include "rgb_lcd.h"

rgb_lcd lcd;
String previous="";
String data="Hello";

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  lcd.begin(16, 2);
  lcd.setRGB(0, 0, 255);
  lcd.print(data);
  Serial.begin(9600);
  Serial.println("Begin");
}

void loop() {
  if(Serial.available() > 0) {
    digitalWrite(LED_BUILTIN, HIGH);
    lcd.setRGB(0,255,0);
    delay(100);
    previous = data;
    data = Serial.readStringUntil('\n') + "                ";
    delay(400);
    digitalWrite(LED_BUILTIN, LOW);
    lcd.setCursor(0, 0);
    lcd.print(previous);
    lcd.setCursor(0,1);
    lcd.print(data);
    lcd.setRGB(255, 255, 255); 
  }
}
