/* ModulinoKnob_serial.ino

A nice input device
 
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

I am using the free Arduino IDE version 2.3.10

VegasEat  30sep2026
 */

#include <Modulino.h>

// create the class instances (names are up to you)
ModulinoKnob knob;

void setup() {
  // the required begin() methods
  Serial.begin(9600);  // for testing...
  Modulino.begin();
  knob.begin();
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
  delay(550);
}
