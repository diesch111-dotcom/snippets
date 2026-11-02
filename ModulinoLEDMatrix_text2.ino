/* ModulinoLEDMatrix_text2.ino

The 'ModulinoLEDMatrix' module uses a blue 8x12 LED matrix controlled 
via 'charlieplexing' technology. The matrix is driven by the Modulino's 
onboard microcontroller (STM32C011F4), which handles the complex timing 
required for 'charlieplexing' and also provides I2C communication.

The display is code compatible with the Arduino UNO R4 WiFi LED matrix.
It has the ability to change the I2C address via software, allowing
different system configurations.

Methods...
begin(): Initializes I2C communication with the LED Matrix (returns 1 on success)
clear(): Turns off all LEDs

Current consumption	with all LEDs on 200 mA (okay for I2C bus).
Blue LEDs draw less current than red LEDs.

https://docs.arduino.cc/tutorials/modulino-matrix/how-matrix/

I am using the C++ based Arduino IDE version 2.3.10
Use the IDE library manger to install any missing header files

Vegaseat  01nov2026
*/

#include <ArduinoGraphics.h>
#include "Modulino_LED_Matrix.h"

// ModulinoLEDMatrix object
ModulinoLEDMatrix matrix;

String message = " Antenne Bayern ----  ";
int charWidth = 4;
int textWidth;
int xPos = 12;

void setup() {
  // Note: Do NOT use the common Modulino.begin();

  // Initializes matrix and I2C bus
  matrix.begin(); 
  // set total text width 
  textWidth = message.length() * charWidth;
}

void loop() {
  matrix.beginDraw();

  matrix.clear();
  // full color
  matrix.stroke(255);
  //matrix.textFont(Font_4x6);
  matrix.textFont(Font_5x7);
  
  matrix.beginText(xPos, 1, 255);
  matrix.print(message);
  matrix.endText();
  
  matrix.endDraw();
  
  xPos--;
  if (xPos < -textWidth) {
    xPos = 12;
  }
  
  delay(100);
}
