/* ModulinoDistance_leds.ino

Using the Arduino Plug and Make kit.
Daisy-chain the ModulinoPixels and the ModulinoDistance modules with the provided 
5-cm Qwiic cable to the 'Qwiic' connector on the 'UNO R4 WiFi' right side.
 
The Modulino distance sensor uses Time-of-Flight (ToF) technology to measure
distances accurately by measuring the time it takes for a beam of laser IR 
light to reflect back from a reflective object eg. hold your hand above the 
module (the sensing cone is narrow).
 
Distance sensor specifications:
Measurement range: Typically 0mm to 4000mm (4 meters)
Accuracy: 3% of distance
 
The available() method checks if a new measurement is ready before
reading to ensure you get fresh data.

The ModulinoPixels module has 8 individual RBG LEDs in a row, each of them 
adjustable to color and brightness.  Use predefined colors like RED, GREEN, 
BLUE, WHITE, YELLOW, CYAN, VIOLET and BLACK (BLACK meaning off).
Different pixels are lit as distance changes,

see:
https://github.com/arduino-libraries/Arduino_Modulino/tree/main/examples/Modulino_Distance
https://github.com/arduino-libraries/Arduino_Modulino/tree/main/examples/Modulino_Pixels

If need be...
Install Modulino.h   (all) with the Library Manager

I am using the free Arduino IDE version 2.3.10

modified by...
VegasEat  01oct2026
*/

#include <Arduino_Modulino.h>

// create the class instances
ModulinoDistance distance;
ModulinoPixels pixels;

void setup() {
  // the required begin() methods
  Serial.begin(9600);  // testing...
  Modulino.begin();
  distance.begin();
  pixels.begin();

  // clear out any old settings
  pixels.clear();
  pixels.show();  // push changes to the LEDs
}

void loop() {
  // Hold a solid object above module (has a narrow cone of detection)
  // Check if new distance measurement is available
  // This ensures we only read when fresh data is ready
  if (distance.available()) {
    // Get the latest distance measurement in millimeters
    // convert to centimeters
    int dist_cm = distance.get() / 10;
    Serial.print(dist_cm);
    Serial.println(" cm");

    // use integers
    switch (dist_cm) {
      case 1:
        pixels.set(0, BLUE);  // default intensity is 5
        break;  // prevents fallthrough
      case 2:
        pixels.set(1, CYAN);
        break;  // prevents fallthrough
      case 3:
        pixels.set(2, YELLOW);
        break;
      case 4:
        pixels.set(3, GREEN);
        break;
      case 5:
        pixels.set(4, WHITE);
        break;
      case 6:
        pixels.set(5, VIOLET);
        break;
      case 7:
        pixels.set(6, RED, 4);
        break;
      case 8:
      case 9:
      case 10:
        pixels.set(7, RED, 40);
        break;
      default:  // Executed if no case matches
        break;
    }
    pixels.show();  // push changes to the LEDs
  }

  // Small millisecond delay to control measurement frequency
  delay(100);
  // clear out any old settings
  pixels.clear();
  pixels.show();  // push changes to the LEDs
}