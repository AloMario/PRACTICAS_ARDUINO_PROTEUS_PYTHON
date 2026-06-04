const int sensorGas = 7;

void setup() {
  pinMode(sensorGas, INPUT);
  Serial.begin(9600);
}

void loop() {
  int valor_sensor = digitalRead(sensorGas);
  Serial.print("Sensor: ");
  Serial.println(valor_sensor);
  delay(1000);

}

