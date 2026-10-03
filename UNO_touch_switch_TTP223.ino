/* UNO_touch_switch_TTP223.ino

toggle ON/OFF by touching the TTP223 sensor board touch circles,
works via capacitance (body to sensor), touch implies HIGH
The sensor board has a pull_down resistor and a green power_on LED.

pins are (left to right):
GND  VCC  Signal

Optional...
Using a 1 MΩ resistor between a send and receive pin (e.g., D2 → D4) 
and a metal electrode, you can build a touch switch using the 
CapacitiveSensor library:  #include <Arduino_CapacitiveTouch.h>

VegasEat  22sep2026
*/

const int touchPin = 2;
const int ledPin = 13;

bool state = false;
bool last = LOW;

void setup() {
  // a pull_down resitor is on the board
  pinMode(touchPin, INPUT);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  bool reading = digitalRead(touchPin);

  if (reading == HIGH && last == LOW) {
    state = !state;              // toggle
    digitalWrite(ledPin, state);
    delay(200);                  // debounce
  }

  last = reading;
}

/* momentary ON version

const int touchPin = 2;
const int ledPin = 8;

void setup() {
  pinMode(touchPin, INPUT);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  digitalWrite(ledPin, digitalRead(touchPin));
}

*/
