/* modulino_matrix_basic.ino

The Modulino LED Matrix module uses an 8×12 LED matrix controlled via 
charlieplexing technology. The LEDs do not have native I²C capabilities. 
Instead, the matrix is driven by the Modulino's onboard microcontroller 
(STM32C011F4), which handles the complex timing required for charlieplexing 
and provides I²C communication.

The display provides the same functionality as the Arduino® UNO R4 WiFi 
LED matrix, ensuring code compatibility.  One unique feature of this setup 
is the ability to change the I²C address via software, making it adaptable 
to different system configurations.

begin(): Initializes I2C communication with the LED Matrix (returns 1 on success)
setFrame(buffer): Displays a single frame on the matrix (accepts predefined 
   icons or custom data)
setSequence(frames): Loads an animation sequence into the matrix 
play(looping): Plays the loaded animation sequence (blocking, optional looping parameter)
nextFrame(): Advances to the next frame in a sequence (non-blocking)
clear(): Turns off all LEDs
setMode(DisplayMode): Sets the display mode (MonochromaticVertical, 
    MonochromaticHorizontal, or Grayscale)

https://docs.arduino.cc/tutorials/modulino-matrix/how-matrix/

Current Consumption	Peak (All LEDs)	200	mA

VegasEat  13oct2026
*/

#include "Modulino_LED_Matrix.h"
#include "LEDMatrixGallery.h" // This header contains predefined animations for the LED matrix display.

ModulinoLEDMatrix matrix;

void setup() {
  if (!matrix.begin()) {
    // If initialization fails, we enter an infinite loop and
    // blink the built-in LED to indicate an error.
    while (true){
      digitalWrite(LED_BUILTIN, !digitalRead(LED_BUILTIN)); // Blink built-in LED to indicate error
      delay(500);
    }
  }
}

void loop() {
  // Play startup animation from gallery
  matrix.setSequence(LEDMATRIX_ANIMATION_STARTUP);
  matrix.play();
  delay(500);

  // Show the UNO icon from the gallery
  matrix.setFrame(LEDMATRIX_UNO);
  delay(1000);

  // Clear the display
  matrix.clear();
  delay(500);
}