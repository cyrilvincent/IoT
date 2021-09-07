int button = A0;
int potar;
float angle;


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
  else
  {
    digitalWrite(LED_BUILTIN, HIGH);
  }
  delay(1000);
}


 
