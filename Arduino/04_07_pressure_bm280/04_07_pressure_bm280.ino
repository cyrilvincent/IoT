#include "Seeed_BME280.h"

// Plug on port I2C
// http://wiki.seeedstudio.com/Grove-Barometer_Sensor-BME280/
// Unit: Pa
BME280 bme280;
 
void setup(void)
{
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
  Serial.println("Starting preasure BM280");
  delay(1000);
  int i = bme280.init();
  Serial.println("pressure:"+String(i)); 
}

void loop(void)
{
    float pre = bme280.getPressure();
    Serial.print("pressure:"+String(pre));
    float temp = bme280.getTemperature();
    Serial.print(" temperature:"+String(temp));
    float hum = bme280.getHumidity();
    Serial.println(" humidity:"+String(hum));
    digitalWrite(LED_BUILTIN, HIGH);
    delay(200);
    digitalWrite(LED_BUILTIN, LOW);
    delay(4800);
}
