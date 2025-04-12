int led = 3; 
int button = 7;
bool isOk = false;
int potar = A2;

void setup() {
  Serial.begin(9600);
  pinMode(led, OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(button, INPUT_PULLUP);
  pinMode(potar, INPUT);
}


void loop() {
  int potarValue = analogRead(potar); // 10 bits = 1024
  // Serial.println(value);
  float ledValue = potarValue / 4; // 8 bits = 256, like potarValue << 2
  Serial.println(ledValue);
  analogWrite(led, ledValue);
  isOk = digitalRead(button);
  digitalWrite(LED_BUILTIN, isOk ? HIGH : LOW);
  delay(100);
}


 
