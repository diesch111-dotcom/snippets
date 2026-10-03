/* UNO_DHT11_sensor_serial.ino

the 3 pin board ...
   (l to r)
   pin1 = GND
   pin2 = data 
   pin3 = Vcc (+5V)

  celcius c to fahrenheit f conversion formula choices
  f = (9/5.0) * c + 32
  c = (5.0/9) * (f - 32)

  degree_symbol = " \xC2\xB0"

VegasEat  02oct2026
*/

#include <DHT.h>

#define DHTPIN  2
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  Serial.println("KY-015 DHT11 Temperature & Humidity Sensor");
  dht.begin();
}

void loop() {
  // Adafruit DHT library enforces a 2-second minimum between reads
  delay(2000);

  float humidity     = dht.readHumidity();
  float temperatureC = dht.readTemperature();
  float temperatureF = dht.readTemperature(true);

  if (isnan(humidity) || isnan(temperatureC)) {
    Serial.println("Error: failed to read from DHT sensor. Check wiring and pull-up.");
    return;
  }

  Serial.print("Humidity: ");
  Serial.print(humidity);
  Serial.print(" %  |  Temperature: ");
  Serial.print(temperatureC);
  Serial.print(" °C  /  ");
  Serial.print(temperatureF);
  Serial.println(" °F");
}
