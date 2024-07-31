#include<dht.h>

dht DHT;

#define DHT11_PIN A1

float min_t,max_t;

void setup()
{
  Serial.begin(9600);
  Serial.print("\nHumidity(%)\tTemperature(C)\tTemperature(C)\tMinTemp\tMaxTemp");
  min_t = 0xffff;
  max_t = 0x00;
}

void loop()
{
  int chk = DHT.read11(DHT11_PIN);
  Serial.print(DHT.humidity,1);
  Serial.print("\t");
  Serial.print(DHT.temperature,1);
  if(DHT.temperature<min_t)
    min_t = DHT.temperature;
  if(DHT.temperature>max_t)
    max_t = DHT.temperature;
  Serial.print("\t");
  Serial.print((DHT.temperature*1.8)+32,1);
  Serial.print("\t");
  Serial.print(min_t);
  Serial.print("\t");
  Serial.print(max_t);
  Serial.print("\n");
}

/*#include <dht.h>

dht DHT;

#define DHT11_PIN A1

float min_t, max_t;

void setup() {
  Serial.begin(9600);
  Serial.println("Humidity(%)\tTemperature(C)\tTemperature(F)\tMinTemp\tMaxTemp");
  min_t = 100.0;
  max_t = -100.0;
}

void loop() {
  int chk = DHT.read11(DHT11_PIN);
  float temperature_C = DHT.temperature;
  float temperature_F = (temperature_C * 1.8) + 32.0;

  if (temperature_C < min_t) {
    min_t = temperature_C;
  }

  if (temperature_C > max_t) {
    max_t = temperature_C;
  }

  Serial.print(DHT.humidity, 1);
  Serial.print("\t");
  Serial.print(temperature_C, 1);
  Serial.print("\t");
  Serial.print(temperature_F, 1);
  Serial.print("\t");
  Serial.print(min_t, 1);
  Serial.print("\t");
  Serial.print(max_t, 1);
  Serial.println();
  
  delay(1000);
}
*/
