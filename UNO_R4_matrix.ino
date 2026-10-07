/* UNO_R4_matrix-vector.ino

Exploring C++ on the Arduino:
Displaying a C++ vector on the Arduino R4 WiFi matrix

I am using the C++ based Arduino IDE version 2.3.10
If you get a missing header error...
Install the needed header file with the IDE's Library Manager

VegasEat  04oct2026
*/

// matrix headers in that order...
#include "ArduinoGraphics.h"
#include "Arduino_LED_Matrix.h"
// normal CPP related header
#include <vector>

// create the class instance
ArduinoLEDMatrix matrix;

void setup() {
  // the required begin
  Serial.begin(9600);  // testing...
  matrix.begin();
  // just a moment
  delay(100);
}

void loop() {
  // vector initialize
  std::vector<int> numbers;
  //std::vector<int> numbers = { 10, 20, 30 };

  // add more elements
  numbers.push_back(40);
  numbers.push_back(50);
  numbers.push_back(60);
  numbers.push_back(70);

  // use the UNO R4 WiFi LED matrix to show results
  // replaces std::cout << ...
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
  for (int num : numbers) {
    matrix.print(num);
    matrix.print(" ");
  }
  // set to scroll to the left
  matrix.endText(SCROLL_LEFT);
  // update the display
  matrix.endDraw();
}
