const int trigger = 7;
const int echo = 6;
const int led = 5;

long duracion;
float distancia;

void setup() {
  pinMode(trigger, OUTPUT);
  pinMode(echo, INPUT);
  pinMode(led, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  digitalWrite(trigger, LOW);
  delayMicroseconds(2);
  digitalWrite(trigger, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigger, LOW);

  duracion = pulseIn(echo, HIGH);
  distancia = duracion * 0.0343 / 2;

  Serial.print("Distancia: ");
  Serial.println(distancia);

  if (distancia < 100) {
    digitalWrite(led, HIGH);
  } else {
    digitalWrite(led, LOW);
  }
  delay(1000);
}
