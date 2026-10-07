/* UNO_CPP_while.ino

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
  // initialize serial communications at 9600 bps
  Serial.begin(9600);  // for testing...
  matrix.begin();
  // just a moment
  delay(100);
}

void loop() {
  // vector initialize
  std::vector<int> numbers;

  int k = 0;
  while (k < 10) {
    k++;
    if (k == 3) continue;  // Skip 3
    if (k == 7) break;     // Exit loop when k hits 7
    numbers.push_back(k);
  }
  // output {1, 2, 4, 5, 6}

  // use the UNO R4 WiFi LED matrix to show results
  matrix.beginDraw();
  // milliseconds/frame, adjust to a rate you like
  matrix.textScrollSpeed(100);
  // set font to 5x7 pixels
  matrix.textFont(Font_5x7);
  // text at position (0, 1)
  matrix.beginText(0, 1, 0xFFFFFF);
  // replaces std::cout << num << " ";
  for (int num : numbers) {
    matrix.print(num);
    matrix.print(" ");
  }
  // set to scroll to the left
  matrix.endText(SCROLL_LEFT);
  // update the display
  matrix.endDraw();
}
