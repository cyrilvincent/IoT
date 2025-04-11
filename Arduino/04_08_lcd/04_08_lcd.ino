#include <Wire.h>
#include "rgb_lcd.h"

rgb_lcd lcd;

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  lcd.begin(16, 2);
  lcd.setRGB(0, 0, 255);
  lcd.print("Begin");
  Serial.begin(9600);
  Serial.println("Begin");
}

void loop() {
  if(Serial.available() > 0) {
    digitalWrite(LED_BUILTIN, HIGH);
    lcd.setRGB(0,255,0);
    delay(100);
    String data = Serial.readStringUntil('\n');
    delay(400);
    digitalWrite(LED_BUILTIN, LOW);
    lcd.print(data);
    lcd.setRGB(255, 255, 255); 
  }
}
