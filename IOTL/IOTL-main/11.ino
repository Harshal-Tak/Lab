#include<dht.h>

dht DHT;

#define DHT11_PIN A1

float min_t,max_t;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.println("Humidity(%)/tTemperatur(C)/tTemperature(F)");
  min_t = 0xffff;
  max_t = 0x00;
}

void loop() {
  // put your main code here, to run repeatedly:
  int chk = DHT.read11(DHT11_PIN);
  Serial.println(DHT.humidity,1);
  Serial.print("\t");
  Serial.print(DHT.temperatue,1);
  Serial.print("\t");
  Serial.print((DHT.temperature*1.8)+32,1);
  delay(1000);

}
