/* ModulinoDistance_matrix.ino

Exploring the Arduino Plug and Make kit:
Attach the Distance Module with the provided 5-cm Qwiic cable to 
the white 'Qwiic' connector on the UNO R4 WiFi right side.

Display the distance in mm or cm on the UNO R4 Wifi
12x8 LED matrix scrolling right to left.
 
The distance sensor uses an infrared laser (940 nm), then Time-of-Flight (ToF) 
technology to detect distances accurately by measuring the time it takes for 
the IR laser light to reflect back from a reflective object straight above the unit.
 
Sensor specifications:
Measurement range: Typically 0mm to 1300mm (1.3 meters)
Accuracy: 3% of distance
Measurement unit: Millimeters (mm)

see:
https://docs.arduino.cc/tutorials/modulino-distance/how-distance/
https://github.com/arduino-libraries/Arduino_Modulino/tree/main/examples/Modulino_Distance
https://github.com/arduino-libraries/Arduino_Modulino/blob/main/docs/images/modulino-distance.jpg

I am using the free C++ based Arduino IDE version 2.3.10
If you get a missing header error...
Install the needed header file with the IDE's Library Manager
.
VegasEat  29sep2026
*/

#include <Arduino_Modulino.h>
// in that order...
#include "ArduinoGraphics.h"
#include "Arduino_LED_Matrix.h"

// create the class instances
ModulinoDistance distance;
ArduinoLEDMatrix matrix;

void setup() {
  // the required begin() methods
  Serial.begin(9600);
  Modulino.begin();
  distance.begin();
  matrix.begin();
}

void loop() {
  // Hold a reflective item like your hand above the module (narrow cone of detection)
  // Check if new distance measurement is available
  // This ensures we only read when fresh data is ready
  if (distance.available()) {
    // Get the latest distance measurement in millimeters (mm)
    // Values typically range from 0mm to 1300mm
    int distance_mm = distance.get();
    // show the result in millimeters or centimeters
    int distance_cm = distance_mm / 10;
    Serial.print(distance_mm);
    Serial.println(" mm");

    // convert numeric results to a C++ char array
    char buf[32];
    sprintf(buf, " %dmm", distance_mm);

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
  // Small millisecond delay to control measurement frequency
  delay(10);
}