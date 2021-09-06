#include <math.h>
 
// Variable declaration
const long B = 4275;               // B value of the thermistor
const long R0 = 100000;            // R0 = 100k
const int pinTempSensor = A1;     // Grove - Temperature Sensor connect to A1
int button = A0;
int potentio_read;
float angle_read;


void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
}


void loop() {
//
  potar = analogRead(button);
  Serial.print("Potar = ");
  Serial.println(potar);
  angle = ((float)potar * 300.0) / 1023.0;
  Serial.print("angle = ");
  Serial.println(angle);
  if (potar <= 512)
    {
      digitalWrite(LED_BUILTIN, LOW);
    }
  if (potar >= 512)
    {
      digitalWrite(LED_BUILTIN, HIGH);
    }
  int a = analogRead(pinTempSensor);
  float R = 1023.0/a-1.0;
  R = R0*R;
  float temperature = 1.0/(log(R/R0)/B+1/298.15)-273.15; // convert to temperature via datasheet
  Serial.print("temperature = ");
  Serial.println(temperature);
  delay(1000);
}


 
