int i=2;
bool isPrime=false;

// ESP32 : 100K in 32s

void setup() {
  Serial.begin(115200);
  Serial.println("Prime number calculation");
  display(i++);
}

void loop() {
  isPrime=true;
  for(int div=2;div<int(sqrt(i))+1;div+=2) {
    if(i%div==0) {
      isPrime=false;
      break;
    }
  }
  if(isPrime) {
    display(i);
  }
  i++;
}

void display(int i) {
  Serial.println(i);
}
