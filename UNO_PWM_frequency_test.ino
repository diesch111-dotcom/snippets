/* UNO_PWM_frequency_test.ino

  The Arduino UNO R4 has 14 digital IO pins
  pins 2 to 13 (pin13 has an indicator LED)
  pins d0 (RX in) and d1 (TX out) are for serial IO
  6 pins have PWM ~3, ~5, ~6, ~9, ~10, ~11
  (PWM is short for Pulse Width Modulation)
  Set PWM to 50% (127 of 254) to generate a squarewave

  VegasEat  25sep2026
*/

// include ArduinoGraphics.h before Arduino_LED_Matrix.h
#include "ArduinoGraphics.h"
#include "Arduino_LED_Matrix.h"

// create the class instance
ArduinoLEDMatrix matrix;

long pulse_high;
long pulse_low;
long time2;
long frequency;

const int input = A0;
// connect pin ~3 t0 analog pin A0
// ~3 PWM pin uses about 500 Hz pulse
const int pwm3 = 3;
// 8bit 254/2 gives a square wave, half time HIGH, half time LOW
const int pwm_value = 127;
void setup() {
  // needed...
  matrix.begin();

  pinMode(input, INPUT);
  pinMode(pwm3, OUTPUT);
}

void loop() {
  // create a squarewave on PWM pin3
  analogWrite(pwm3, pwm_value);
  // measure duration in microseconds of pulse being HIGH
  pulse_high = pulseIn(input, HIGH);
  // measure duration in microseconds of pulse being LOW
  pulse_low = pulseIn(input, LOW);
  // total duration squarewave pulse in microseconds
  time2 = pulse_high + pulse_low;
  // frequency in Herz from inverse duration in microseconds
  frequency = 1000000 / time2;

  if (frequency > 0) {
    // scroll longer text
    matrix.beginDraw();
    // rate = ms/frame
    matrix.textScrollSpeed(200);
    matrix.textFont(Font_4x6);
    // x, y, color
    matrix.beginText(0, 1, 0xFFFFFF);
    char buf[20];
    sprintf(buf, " %d Hertz  ", int(frequency));
    matrix.println(buf);
    // set scroll direction
    matrix.endText(SCROLL_LEFT);
    matrix.endDraw();
  }
  delay(500);
}
