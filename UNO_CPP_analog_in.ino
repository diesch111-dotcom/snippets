/* UNO_CPP_analog_in.ino

Exploring C++ on the Arduino:
Processing a voltage analog input
(use a jumber wire from the Arduino +3.3V pin to an analog input pin)
displaying/scrolling the measurement on the Arduino R4 WiFi matrix

Do not exceed +5.5V at any Arduino input pin!

I am using the C++ based Arduino IDE version 2.3.10
Help/Reference brings up potential built-in C++ details

If you get a missing header error...
Install the needed header file with the IDE's Library Manager

VegasEat  05oct2026
*/

// matrix headers in that order...
#include "ArduinoGraphics.h"
#include "Arduino_LED_Matrix.h"

// create the class instance
ArduinoLEDMatrix matrix;

int voltPin = A0;  // connect +3.3V pin to analog pin A0 (jumber wire)

void setup() {
  // initialize serial communications at 9600 bps
  Serial.begin(9600);  // extra for testing...
  matrix.begin();
  pinMode(voltPin, INPUT);
  // just a moment
  delay(10);
}

void loop() {
  // read the input on the specified Arduino analog pin
  int sensorValue1 = analogRead(voltPin);
  // convert the 10bit (1023 max) reading to volts
  float volts = sensorValue1 * (5.0 / 1023.0);

  // use the UNO R4 WiFi LED matrix to show results
  matrix.beginDraw();
  // milliseconds/frame, adjust to a rate you like
  matrix.textScrollSpeed(100);
  // set font to 5x7 pixels
  matrix.textFont(Font_5x7);
  // text at position (0, 1)
  matrix.beginText(0, 1, 0xFFFFFF);
  // replaces std::cout << "  " << volts << " V";
  matrix.print("  ");
  matrix.print(volts);
  matrix.print(" V");
  // set to scroll to the left
  matrix.endText(SCROLL_LEFT);
  // update the display
  matrix.endDraw();
}
