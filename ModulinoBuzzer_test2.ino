/* ModulinoBuzzer_test2.ino

'ModulinoBuzzer is a small 'Piezoelectric' most likely ceramic element 
that functions as an earphone sized speaker. It is one of the plug and make 
Modulino boards recognizable by a centered black plastic square and a speaker 
symbol.  The problems is all mine,  At my age much of my hearing is weak.
So I won't use it much, unless the Arduino engineers can make it much louder!
Well, make me a liar, I can hear it somewhat holding it close to my good ear!

Some specs:
Frequency range: approximately 20Hz to 20,000Hz (20kHz)
Common musical note frequencies:
C4 (Middle C): 262 Hz
A4 (Concert pitch): 440 Hz
C5: 523 Hz

info...
https://github.com/arduino-libraries/Arduino_Modulino/blob/main/examples/Modulino_Buzzer

I am using the C++ based Arduino IDE version 2.3.10

VegasEat  16oct2026
*/

#include <Arduino_Modulino.h>

// Create a ModulinoBuzzer object
ModulinoBuzzer buzzer;

// Frequency in Hertz (Hz) 440Hz is the musical note A4
int frequency = 440;
// Duration in milliseconds (ms) how long the tone plays
int duration = 1000;

void setup(){
  // the required begin() methods
  // Initialize Modulino I2C bus communication
  Modulino.begin();
  buzzer.begin();
}

void loop(){
  // Play some tone with specified frequency and duration
  buzzer.tone(frequency, duration);
  // Wait ...can you hear me?  ...can you hear me now?
  delay(1000);
  
  // Stop the tone by setting the frequency to 0
  buzzer.tone(0, duration);
  // Wait another second in silence before repeating
  delay(1000);
}
