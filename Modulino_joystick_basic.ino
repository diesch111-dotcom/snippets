/* Modulino_joystick_basic.ino

The Modulino Joystick module features an analogue joystick with two potentiometers 
(horizontal and vertical axes) and an integrated push button. The joystick does 
not have native I²C capabilities. Instead, the readings are processed by the 
Modulino's onboard microcontroller (STM32C011F4), which provides I²C communication.

update(): Updates joystick state, returns true if values changed
getX(): Returns horizontal position (-128 to 127, centre = 0)
getY(): Returns vertical position (-128 to 127, centre = 0)
isPressed(): Returns button state (HIGH when pressed)
setDeadZone(threshold): Sets the centre dead zone threshold (default 26)

https://docs.arduino.cc/tutorials/modulino-joystick/how-joystick/

VegasEat  13oct2026
*/

#include <Modulino.h>

ModulinoJoystick joystick;

void setup() {
  Serial.begin(9600);
  Modulino.begin();
  joystick.begin();
}

void loop() {
  // Update joystick readings
  if (joystick.update()) {
    // Read X and Y axes (range: -128 to 127)
    int8_t x = joystick.getX();
    int8_t y = joystick.getY();
    
    // Check button state
    bool pressed = joystick.isPressed();
    
    // Display readings
    Serial.print("X: ");
    Serial.print(x);
    Serial.print("\tY: ");
    Serial.print(y);
    Serial.print("\tButton: ");
    Serial.println(pressed ? "PRESSED" : "Released");
  }
  
  delay(50);
}
