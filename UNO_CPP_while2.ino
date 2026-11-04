/* UNO_CPP_while2.ino

Exploring C++ on the Arduino:
Displaying a C++ vector on the Arduino R4 WiFi 12x8 matrix.
A C++ vector allows you to change elements and size (array is fixed).

Optimize via static heap allocation (avoids heap fragmentation over time),
also load the vector once in setup()
Using the C++ based Arduino IDE version 2.3.10

Vegaseat  03nov2026
*/

// matrix headers in that order...
#include "ArduinoGraphics.h"
#include "Arduino_LED_Matrix.h"
// normal CPP related header
#include <vector>

// create the class instance
ArduinoLEDMatrix matrix;

// empty vector initialize
// use static to allocate heap memory
static std::vector<int> numbers;

void setup() {
  matrix.begin();

  // load the vector via push_back()
  int k = 0;
  while (k < 10) {
    k++;
    if (k == 3) continue;  // Skip 3
    if (k == 7) break;     // Exit loop when k hits 7
    numbers.push_back(k);
  }  // output {1, 2, 4, 5, 6}
}

void loop() {
  // use the UNO R4 WiFi LED matrix to show results
  matrix.beginDraw();
  // milliseconds/frame, adjust to a rate you like
  matrix.textScrollSpeed(100);
  // set font to 5x7 pixels
  matrix.textFont(Font_5x7);
  // text at position (0, 1, full color, here red LED)
  matrix.beginText(0, 1, 0xFFFFFF);
  // replaces std::cout << num << " ";
  // use range based for loop
  for (int num : numbers) {
    matrix.print(num);
    matrix.print(" ");
  }
  // set to scroll to the left
  matrix.endText(SCROLL_LEFT);
  // update the display
  matrix.endDraw();
}
