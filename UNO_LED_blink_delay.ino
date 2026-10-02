/* UNO_LED_blink_delay.ino

Exploring an Arduino UNO programmable controller:
A standard test, the "Hello Wprld" of Arduino!
Turn a LED on, then off repeatedly for a given delay time.
Timing is done via the delay() function, which blocks other action
while it is delaying!

docs
https://docs.arduino.cc/tutorials/uno-rev3/intro-to-board/

Optionally connect an extra LED...
Long leg (anode) via a 330 ohm current limiting resistor to IO pin 13
Short leg (cathode, also plastic has flat section there) to GND

I am using the free C++ based Arduino IDE version 2.3.10

VegasEat  24sep2026
*/

long wait = 1000;  // wait/delay time in milliseconds

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN (pin 13) as an output.
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH);
  delay(wait);
  digitalWrite(LED_BUILTIN, LOW);
  delay(wait);
}
