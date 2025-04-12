#include <Wire.h>
#include "Seeed_BME280.h"
int address = 0x76;

void setup()
{
  Wire.begin();
  Serial.begin(9600);
  Serial.println("Begin I2C");
  Serial.print("Scan I2C @");
  Serial.println(address, HEX);
}

void loop(void)
{
    Serial.print("BME280_REG_CHIPID: ");
    Serial.println(BME280_REG_CHIPID, HEX);
    Wire.beginTransmission(address);
    Wire.write(BME280_REG_CHIPID);
    Wire.endTransmission();
    Wire.requestFrom(address, 1);
    int chip_id = 0;
    if (Wire.available() < 1) {
        Serial.println("Not available");
    }
    else {
        chip_id = Wire.read();
    }
    Serial.print("Chip id: ");
    Serial.println(chip_id, HEX);

    delay(1000);
}

