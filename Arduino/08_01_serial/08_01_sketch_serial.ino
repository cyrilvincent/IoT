void setup()
{
    Serial.begin(9600);
    Serial.println("Listen...");
}

void loop()
{
    if (Serial.available() > 0) {
      String message = Serial.readStringUntil('\n');
      Serial.println("Hello "+message);
    }
}
