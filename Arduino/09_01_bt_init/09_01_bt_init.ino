#include <SoftwareSerial.h>

#define RxD 6
#define TxD 7

SoftwareSerial blueToothSerial(RxD,TxD);

void setup()
{
    Serial.begin(9600);
    Serial.println("Init BT"); 
    blueToothSerial.begin(9600);
    delay(1000);
    blueToothSerial.print("AT");
    delay(400); 
    blueToothSerial.print("AT+DEFAULT"); // Restore all setup value to factory setup
    delay(2000); 
    blueToothSerial.print("AT+NAMEcyrilbt"); // set the bluetooth name as "SeeedMaster" ,the length of bluetooth name must less than 12 characters.
    delay(1000);
    blueToothSerial.print("AT+PIN1234"); // PIN Code default 1234           
    delay(400);    
    blueToothSerial.print("AT+AUTH0");   // No Auth     
    delay(400);
    blueToothSerial.flush();
    delay(1000);
    Serial.println("End Init BT"); 
}

void loop()
{
  blueToothSerial.println("Hello from cyrilbt");
  delay(1000);
}
