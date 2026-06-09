const int trigger = 7;
const int echo = 6;
long duracion;
float distancia;

void setup() {
  pinMode(trigger, OUTPUT);
  pinMode(echo, INPUT);
  Serial.begin(9600);
}

void loop() {
  // Generar pulso ultrasónico
  digitalWrite(trigger, LOW);
  delayMicroseconds(2);
  digitalWrite(trigger, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigger, LOW);

  // Medir tiempo de retorno
  duracion = pulseIn(echo, HIGH);

  // Calcular distancia en centímetros
  distancia = duracion * 0.0343 / 2;
  // Mostrar resultado
  Serial.print("Distancia: ");
  Serial.println(distancia);
  delay(1000);
}
