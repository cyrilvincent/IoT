#include <math.h>

// Temp sensor
// Voltage 3.3/5
// Analog
// Range -40°C +125°C
// Precision +-1.5°C

const long B = 4275;               
const long R0 = 100000;            
const long tempPin = A1; //A6;     

void setup()
{
    Serial.begin(9600);
}

void loop()
{
    int a = analogRead(tempPin);
    float R = 1023.0/a-1.0;
    R = R0*R;
    float temperature = 1.0/(log(R/R0)/B+1/298.15)-273.15; // convert to temperature via datasheet for 5V
    Serial.println(temperature); // Arduino Precision = 0.08, sensor precision = 1.5
    delay(1000);
}
