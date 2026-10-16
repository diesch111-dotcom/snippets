/* ModulinoThermo_serial2.ino

The 'ModulinoThermo' can read temperature and humidity. It is one 
of the plug and make Modulino boards recognizable by a thermometer 
and drop of water (drop of sweat?) symbol.

To see changes, hold your hand near the center sensing element.

Temperature: Measured in degrees Celsius
Range: minus 40 C to 85 C
Accuracy: 0.2 C

Humidity: Measured in relative humidity percentage (rH%)
Range: 0% to 100%
Accuracy: 2%

see:
https://github.com/arduino-libraries/Arduino_Modulino/tree/main/examples/Modulino_Thermo

I am using the C++ based Arduino IDE version 2.3.10

VegasEat  15oct2026
*/


#include <Modulino.h>

// Create an object/instance
ModulinoThermo thermo;

void setup() {
  // the necessary begin() methods 
  Serial.begin(9600);   // to show our results...
  Modulino.begin();
  thermo.begin();
}

void loop() {
  // Read temperature in Celsius from the sensor
  float celsius = thermo.getTemperature();

  // Convert Celsius to Fahrenheit
  float fahrenheit = (celsius * 9 / 5) + 32;

  // Read relative humidity percentage from the sensor
  // Returns values from 0.0 to 100.0
  float humidity = thermo.getHumidity();

  // Convert numeric results to a char array
  char buf[40];
  sprintf(buf, " %0.1fC  %0.1fF  %0.1frH%%", celsius, fahrenheit, humidity);

  Serial.println(buf);
  // measure every 5 seconds = 5000 milliseconds
  delay(5000);
}
