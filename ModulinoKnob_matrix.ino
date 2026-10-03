/* ModulinoKnob_matrix.ino
 
Exploring the Arduino Plug and Make kit:
Attach the ModulinoKnob module with the provided 5-cm Qwiic cable to the white 'Qwiic'
connector on the UNO R4 WiFi right side.  Now you can read position, button press, and 
rotation direction from the Modulino Knob (a rotary encoder).  The knob turns in distinct 
counted steps/positions. These values increment or decrement with each turn depending on 
the direction of the turn.  Values Increase when rotated clockwise, decrease when rotated 
counter-clockwise,  They can be positive or negative (no fixed range),

The knob shaft activates a pushbutton when pressed.

see...
https://github.com/arduino-libraries/Arduino_Modulino/tree/main/examples/Modulino_Knob

If need be...
Install header files with the Library Manager

VegasEat  30sep2026
 */

#include <Modulino.h>
// in that order...
#include "ArduinoGraphics.h"
#include "Arduino_LED_Matrix.h"

// create the class instances (names are up to you)
ModulinoKnob knob;
ArduinoLEDMatrix matrix;

void setup() {
  // the required begin() methods
  Serial.begin(9600);  // for testing...
  Modulino.begin();
  knob.begin();
  matrix.begin();
  // start at position zero
  knob.set(0);
}

void loop() {
  // Get the current position value of the knob,
  // increments when turned clockwise, decrements when turned counter-clockwise
  long position = knob.get();

  // Print the current position value
  Serial.print("Current position is: ");
  Serial.println(position);

  // Get the rotation direction since last check
  // Returns: 1 for clockwise, -1 for counter-clockwise, 0 for no rotation
  int direction = knob.getDirection();

  // Print rotation direction
  if (direction == 1) {
    Serial.println("Rotated clockwise");
  } else if (direction == -1) {
    Serial.println("Rotated counter-clockwise");
  }

  // optionally limit the range
  if (position > 1000 || position < -1000) {
    knob.set(0);  // eset to 0 if outside range
  }

  // Check if the knob has been pressed
  // returns true after a press, then false until next press
  if (knob.isPressed()) {
    Serial.println("Knob pressed!");
    // optionally reset knob position to zero
    knob.set(0);
  }

  // Display the position on the LED matrix
  // convert numeric results to a char array
  char buf[32];
  sprintf(buf, " %d ", position);
  // use the 'UNO R4 WiFi' LED matrix
  matrix.beginDraw();
  // milliseconds/frame, this affects button press
  // need to press button longer then frame rate
  matrix.textScrollSpeed(50);
  // set font to 5x7 pixels
  matrix.textFont(Font_5x7);
  // text at position (0, 1)
  // a color value is needed even though LEDs are
  // red on the UNO R4 WiFi and blue on the UNO Q
  // top and bottom row of LEDs are not used here
  matrix.beginText(0, 1, 0xFFFFFF);
  // print the position character buffer
  matrix.println(buf);
  // set to scroll to the left
  matrix.endText(SCROLL_LEFT);
  // update the display
  matrix.endDraw();
}