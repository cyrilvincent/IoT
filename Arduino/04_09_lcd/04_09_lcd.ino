#include <Wire.h>
#include "rgb_lcd.h"

rgb_lcd lcd;

void setup() {
    lcd.begin(16, 2);
    lcd.setRGB(255, 0, 0);
    lcd.print("Hello, world!");
    delay(1000);
    lcd.setRGB(255, 255, 255);
}

void loop() {
    lcd.setCursor(0, 1);
    lcd.print(millis() / 1000);
    delay(100);
}

/*********************************************************************************************************
    END FILE
*********************************************************************************************************/