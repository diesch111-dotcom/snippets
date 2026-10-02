/* ModulinoPixels_led_set.ino

Exploring the Arduino Plug and Make kit.
Attach the ModulinoPixels module with the provided 5-cm Qwiic cable to 
the white 'Qwiic' connector on the UNO R4 WiFi or UNO Q right side.

This module has 8 individual RBG LEDs in a row, each of them adjustable to color and
brightness.  There are a number of ways to set the RGB color.  The most versatile is
to give Red, Green, Blue and integer value from 0 to 255 leading to > 1 million choices.
The quickest way is to use predefined colors like RED, GREEN, BLUE, WHITE, YELLOW, 
CYAN, VIOLET and BLACK (BLACK meaning off).

Use the ModulinoPixels method:
  set(int index, int red, int green, int b, int brightness = 5)
where...
index = 0 to 7 (for the 8 LEDs)
color = predefined or red, green, blue integer values
eg,
set(0, RED)  or  set(0, 255, 0, 0)
brightness = 0 to 100 (percent), defaults to 5 (zero % means off)

method clear() turns all pixels off

see...
https://github.com/arduino-libraries/Arduino_Modulino/tree/main/examples/Modulino_Pixels
https://github.com/arduino-libraries/Arduino_Modulino/blob/main/docs/images/modulino-pixels.jpg

If need be...
Install Modulino.h  with the Library Manager

I am using the free C++ based Arduino IDE version 2.3.10

VegasaEat  30sep2026
*/

#include <Modulino.h>

// create the pixels instance/object (name is up to you)
ModulinoPixels pixels;

void setup() {
  // the required begin() stuff
  Modulino.begin();
  pixels.begin();
  
  // clear out any old settings
  pixels.clear();
  pixels.show();  // push changes to the LEDs

  //pisels.set(int index, int r, int g, int b, int brightness = 5)
  // set first pixel (idx = 0) to red
  // r = 255, g = 0, b = 0 implies red
  pixels.set(0, 255, 0, 0, 15);
  // set second pixel (idx = 1) to blue
  pixels.set(1, 0, 0, 255, 40);
  // set third pixel (idx = 2) to green
  pixels.set(2, 0, 255, 0, 25);
  // there are just a few predefined colors
  // like RED, GREEN, BLUE, WHITE, YELLOW, CYAN, VIOLET, BLACK
  // BLACK or brightness = 0 means off
  // set next pixels to a predefined color and default brightness = 5
  pixels.set(3, BLACK);  // off
  pixels.set(4, YELLOW);
  pixels.set(5, WHITE);
  pixels.set(6, CYAN);
  pixels.set(7, VIOLET);
  pixels.show();  // push changes to the LEDs

  // give it some time to look at
  delay(8000);
  pixels.clear();
  pixels.show();  // push changes to the LEDs
}

void loop() {
  // not used
}
