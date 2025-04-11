int led = 3; //LED_BUILTIN;

void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  Serial.begin(9600);
  pinMode(led, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  int i;
  for(i=0;i<256;i++) {
    Serial.println(i);
    analogWrite(led, i);
    delay(10);
  }
  for(i=255;i>-1;i--) {
    Serial.println(i);
    analogWrite(led, i);
    delay(10);
  }
}
