int pin=A1;

void setup() {
  Serial.begin(9600);
  Serial.println("Test PWM without TearDown");
  pinMode(pin, INPUT);
}

void loop() {
  int res = analogRead(pin);  
  Serial.println(res);
  delay(100);
}
