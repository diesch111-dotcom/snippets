/* ModulinoKnob_serial2.ino

The ''ModulinoKnob'' is a handy input device, actually a rotary encoder with
a descriptive name.  It is one of the plug and make Modulino items recognizable
by its big white knob.

A rotary encoder turns in distinct counted steps/positions.  Values increase 
when rotated clockwise, decrease when rotated counter-clockwise, with no fixed 
range.  Think how you can apply those values to your code.

As an extra, the knob shaft activates a push-button when pressed.

info...
https://github.com/arduino-libraries/Arduino_Modulino/tree/main/examples/Modulino_Knob

I am using the C++ based Arduino IDE version 2.3.10

VegasEat  15oct2026
*/

#include <Modulino.h>

// create the class instance
ModulinoKnob knob;

void setup() {
  // the required begin() methods
  Serial.begin(9600);  // for our testing...
  Modulino.begin();
  knob.begin();
  // start at position value zero
  knob.set(0);
}

void loop() {
  // Get the current position value of the knob
  long position = knob.get();

  // Show the current position value
  Serial.print("Current position is: ");
  Serial.println(position);

  // Get the rotation direction since last checked
  // Returns 1 for clockwise, -1 for counter-clockwise, 0 for no rotation
  int direction = knob.getDirection();

  // Show rotation direction
  if (direction == 1) {
    Serial.println("Rotated clockwise");
  } else if (direction == -1) {
    Serial.println("Rotated counter-clockwise");
  }

  // Optionally limit the range
  if (position > 1000 || position < -1000) {
    knob.set(0);  // reset to 0 if outside the range
  }

  // Check if the knob has been pressed
  // Returns true after a press, then false until next press
  if (knob.isPressed()) {
    Serial.println("Knob pressed!");
    // optionally reset knob position to zero
    knob.set(0);
  }
  // for Serial Monitor readability
  delay(100);
}
