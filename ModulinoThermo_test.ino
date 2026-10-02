/* ModulinoThermo_test.ino
 
Exploring the Arduino Plug and Make kit:
Read temperature and humidity with the Modulino Thermo sensor.
Attach the Thermo Module with the provided 4 wire short cable to 
the little white 'Qwiic' connector on the UNO R4 WiFi right edge.

Temperature: Measured in degrees Celsius
Range: minus 40 C to 85 C
Accuracy: 0.2 C

Humidity: Measured in relative humidity percentage (rH%)
Range: 0% to 100%
Accuracy: 2%

see:
https://github.com/arduino-libraries/Arduino_Modulino/tree/main/examples/Modulino_Thermo
https://github.com/arduino-libraries/Arduino_Modulino/blob/main/docs/images/modulino-thermo.jpg

If need be...
Install Modulino.h   (all) with the Library Manager

I am using the free C++ based Arduino IDE version 2.3.10

modified by...
VegasEat  02oct2026
*/

#include <Modulino.h>

// Create object/instance
ModulinoThermo thermo;

void setup() {
  // the necessary begin() methods 
  Serial.begin(9600);
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

  // convert numeric results to a char array
  char buf[32];
  sprintf(buf, " %0.1fC  %0.1fF  %0.1f%%", celsius, fahrenheit, humidity);

  Serial.println(buf);
  // measure every 10 seconds
  delay(10000);
}
