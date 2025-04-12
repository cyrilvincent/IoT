int led = 3; 
int button = 7;
bool isOk = false;

void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  Serial.begin(9600);
  pinMode(led, OUTPUT);
  pinMode(button, INPUT_PULLUP);
}

// the loop function runs over and over again forever
void loop() {
  int i;
  for(i=0;i<256;i++) {
    Serial.println(i);
    isOk = digitalRead(button);
    if(!isOk) {
      analogWrite(led, i);
    }
    delay(10);
  }
  for(i=255;i>-1;i--) {
    Serial.println(i);
    isOk = digitalRead(button);
    if(!isOk) {
      analogWrite(led, i);
    }
    delay(10);
  }
}
