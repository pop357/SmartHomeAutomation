
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>

#define SEALEVELPRESSURE_HPA (1013.25)

Adafruit_BME280 bme; // Kreiranje BME280 objekta

void setup() {
  Serial.begin(9600);
  if (!bme.begin(0x76)) { // Inicijalizacija BME280 senzora
    Serial.println("Could not find a valid BME280 sensor, check wiring!");
    while (1);
  }
}

void loop() {
  float temperature = bme.readTemperature(); // Čitanje temperature u Celzijusima
  float humidity = bme.readHumidity(); // Čitanje relativne vlažnosti u postocima
  float pressure = bme.readPressure() / 100.0F; // Čitanje atmosferskog tlaka u hektopaskalima

  

  Serial.print("Temperature = ");
  Serial.print(temperature);
  Serial.println(" *C");

  Serial.print("Humidity = ");
  Serial.print(humidity);
  Serial.println(" %");

  Serial.print("Pressure = ");
  Serial.print(pressure);
  Serial.println(" hPa");


  delay(5000);
}

