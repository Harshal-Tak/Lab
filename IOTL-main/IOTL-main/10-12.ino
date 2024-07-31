#include<dht.h>

dht DHT;

#define DHT11_PIN A1;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.print("Humidity(%)\tTemperature(C)");
}

void loop() {
  // put your main code here, to run repeatedly:
  int chk = DHT.read11(DHT11_PIN);
  Serial.println(DHT.humidity,1);
  Serial.print("\t");
  Serial.print(DHT.temperature,1);
}
