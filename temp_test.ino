#include <dht11.h>
dht11 DHT;
#define DHT11_PIN 2

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  int chk;
  chk = DHT.read(DHT11_PIN); //Читаем данные с датчика
  Serial.println(DHT.temperature,1);
  delay(3000);
}

