/* ModulinoPixels_customcolors.ino

Using the Arduino Plug and Make kit.
Attach the ModulinoPixels module with the provided 5-cm Qwiic cable to 
the white 'Qwiic' connector on the UNO R4 WiFi or UNO Q right side.

This module has 8 individual RBG LEDs in a row, each of them adjustable to color and
brightness.  There are a number of ways to set the RGB color.  The most versatile is
to give Red, Green, Blue and integer value from 0 to 255 leading to > 1 million choices.

Use the ModulinoPixels method:
  set(int index, int red, int green, int b, int brightness = 5)
where...
index = 0 to 7 (for the 8 LEDs)
color = red, green, blue integer values 0 to 255
brightness = 0 to 100 (percent), defaults to 5 (zero % means off)

ModulinoColor is the type used when you create custom RGB colors.
method clear() turns all pixels off

// Set LED 0 to custom Orange (255, 127, 0) at 50% brightness
leds.set(0, 255, 127, 0, 50);

see...
https://github.com/arduino-libraries/Arduino_Modulino/tree/main/examples/Modulino_Pixels
https://github.com/arduino-libraries/Arduino_Modulino/blob/main/docs/images/modulino-pixels.jpg

I am using the free C++ based Arduino IDE version 2.3.10
If you get a missing header error...
Install the needed header file with the IDE's Library Manager

VegasEat  30sep2026
*/

#include <Modulino.h>

ModulinoPixels leds;

int brightness = 4;

// create a custom colors array
ModulinoColor palette[] = {
  ModulinoColor(255, 218, 185),  // peachPuff
  ModulinoColor(160, 32, 240),   // purple
  ModulinoColor(0, 0, 128),      // navy
  ModulinoColor(255, 215, 0),    // gold
  ModulinoColor(0, 128, 128),    // teal
  ModulinoColor(34, 139, 34),    // forestgreen
  ModulinoColor(250, 128, 114),  // salmon
  ModulinoColor(255, 20, 147)    // hotPink
};

void setup() {
  // the required begin() methods
  Modulino.begin();
  leds.begin();

  // clear out any old settings
  leds.clear();
  leds.show();  // push changes to the LEDs
}

void loop() {
  for (int i = 0; i <= 8; i++) {
    leds.set(i, palette[i], brightness);
    leds.show();
    delay(800);
  }
  // time to look at
  delay(8000);
  leds.clear();
  leds.show();  // push changes to the LEDs
}