#include <SoftwareSerial.h>

const byte rxPin = 2;
const byte txPin = 3;
SoftwareSerial mySerial(rxPin, txPin);

void setup()
{
    Serial.begin(9600);
    mySerial.begin(9600);
    Serial.println("Listen...");
}

void loop()
{
  if (mySerial.available() > 0) {
    Serial.println("Available");
    String message = mySerial.readStringUntil('\n');
    Serial.println("Arduino: "+message);
  }
}
