/* ModulinoThermo_matrix.ino

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

°C (template for the fancy folks)

I am using the free C++ based Arduino IDE version 2.3.10
If you get a missing header error...
Install the needed header file with the IDE's Library Manager

VegasEat  29sep2026
*/

#include <Arduino_Modulino.h>
// in that order...
#include "ArduinoGraphics.h"
#include "Arduino_LED_Matrix.h"

// create the class instances
ModulinoThermo thermo;
ArduinoLEDMatrix matrix;

void setup() {
  // the required begin
  Serial.begin(9600);  // testing...
  Modulino.begin();
  thermo.begin();
  matrix.begin();
  // just a moment
  delay(100);
}

void loop() {
  // Acquire temperature in Celsius and humidity percentage
  float celsius = thermo.getTemperature();
  // Convert Celsius to Fahrenheit
  float fahrenheit = (celsius * 9 / 5) + 32;
  float humidity = thermo.getHumidity();

  // convert numeric results to a char array
  char buf[32];
  //sprintf(buf, " %0.1fC  %0.1f%%", celsius, humidity);
  sprintf(buf, " %0.1fC  %0.1fF  %0.1f%%", celsius, fahrenheit, humidity);

  // use the UNO R4 WiFi LED matrix
  matrix.beginDraw();
  // milliseconds/frame, adjust to a rate you like
  matrix.textScrollSpeed(100);
  // set font to 5x7 pixels
  matrix.textFont(Font_5x7);
  // text at position (0, 1)
  // a color value is needed even though LEDs are 
  // red on the UNO R4 WiFi and blue on the UNO Q
  // top and bottom row of LEDs are not used here
  matrix.beginText(0, 1, 0xFFFFFF);
  // print the temperature and humidity character buffer
  matrix.println(buf);
  // set to scroll to the left
  matrix.endText(SCROLL_LEFT);
  // update the display
  matrix.endDraw();
}