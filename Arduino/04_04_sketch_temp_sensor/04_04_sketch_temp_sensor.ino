// Demo code for Grove - Temperature Sensor V1.1/1.2
// Loovee @ 2015-8-26

#include <math.h>

const long B = 4275;               // B value of the thermistor
const long R0 = 100000;            // R0 = 100k
const long pinTempSensor = A5;     // Grove - Temperature Sensor connect to A0

void setup()
{
    Serial.begin(9600);
    Serial.println("Begin temp sensor 1.2");
}

void loop()
{
    int a = analogRead(pinTempSensor);

    float R = 1023.0/a-1.0;
    R = R0*R;

    float temperature = 1.0/(log(R/R0)/B+1/298.15)-273.15; // convert to temperature via datasheet

    Serial.print("Temperature = ");
    Serial.println(temperature);

    delay(1000);
}
