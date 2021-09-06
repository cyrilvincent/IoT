int button = 2;

void setup() {
  // Setup
  Serial.begin(9600);
  // Main program
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(button, INPUT);
}


void loop() {
//
  int res = digitalRead(port_number_button);
  Serial.println(button_status);
  if (res == 1)
    {
      digitalWrite(LED_BUILTIN, HIGH);
    }
  if (res == 0)
    {
      digitalWrite(LED_BUILTIN, LOW);
    }
}
