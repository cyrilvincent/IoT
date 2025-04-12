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
  isOk = digitalRead(button);
  Serial.println(isOk);
  if(isOk) {
    digitalWrite(led, HIGH);
  }
  else {
    digitalWrite(led, LOW);
  }
}