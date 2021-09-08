#include <SoftwareSerial.h>

#define RxD 6
#define TxD 7

SoftwareSerial blueToothSerial(RxD,TxD);
int i = 0;

void setup()
{
    Serial.begin(9600);
    Serial.println("Starting BT");
    blueToothSerial.begin(9600);
    delay(1000);
}

void loop()
{
    Serial.println(i);
    blueToothSerial.println(i);
    i++;
    delay(1000);

}
