/* UNO_LED_blink_odd_even.ino

Exploring an Arduino UNO programmable controller:
Comvert millis() milliseconds to seconds and use (seconds % 2 == 0) when even
Avoids the blocking delay() function.

docs
https://docs.arduino.cc/tutorials/uno-rev3/intro-to-board/
https://arduinomodules.info/ky-008-laser-transmitter-module/

I am using the free C++ based Arduino IDE version 2.3.10

VegasEat  02oct2026
*/

// optionally connect the gated laser modue KY-008 to pin 13

void setup() {
  // initialize digital pin LED_BUILTIN (pin 13) as an output.
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {

  unsigned long milliseconds = millis();
  unsigned long seconds = milliseconds / 1000;  // 1 second
  // dekasecond or partial dekasecond option
  unsigned long dekaseconds = milliseconds / 10000;  // 10 seconds

  // LED is on when seconds value is even
  if (seconds % 2 == 0) {
    digitalWrite(LED_BUILTIN, HIGH);
  } else {
    digitalWrite(LED_BUILTIN, LOW);
  }
}
