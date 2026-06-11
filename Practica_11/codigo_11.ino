#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

const int potenciometro = A1;
const int echo = 8;
const int trigger = 9;

long duracion;
float distancia;
int valorPot;

void setup() {
  pinMode(trigger, OUTPUT);
  pinMode(echo, INPUT);
  lcd.init();
  lcd.backlight();
  Serial.begin(9600);
}

void loop() {
  // Lectura del potenciómetro
  valorPot = analogRead(potenciometro);

  // Lectura del sensor ultrasónico
  digitalWrite(trigger, LOW);
  delayMicroseconds(2);
  digitalWrite(trigger, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigger, LOW);
  duracion = pulseIn(echo, HIGH);
  distancia = duracion * 0.0343 / 2;

  // Mostrar información en LCD
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Pot:");
  lcd.print(valorPot);
  lcd.setCursor(0, 1);
  lcd.print("Dist:");
  lcd.print(distancia, 1);
  lcd.print("cm");

  // Envío por puerto serial
  Serial.print("ultrasonico,");
  Serial.print(valorPot);
  Serial.print(",distancia,");
  Serial.println(distancia, 1);

  delay(500);
}