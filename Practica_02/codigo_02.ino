const int sensor = A0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int valor_sensor = analogRead(sensor);
  Serial.print("Sensor: ");
  Serial.println(valor_sensor);
  delay(1000);
}
