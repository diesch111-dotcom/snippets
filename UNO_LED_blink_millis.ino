/* UNO_LED_blink_millis.ino

Exploring an Arduino UNO programmable controller:
Blink via millis() function 
currentMillis
previousMillis
interval
Avoids the blocking delay() function

docs
https://docs.arduino.cc/tutorials/uno-rev3/intro-to-board/

Optionally connect an extra LED...
Long leg (anode) via a 330 ohm current limiting resistor to IO pin 13
Short leg (cathode, also plastic has flat section there) to GND

I am using the free C++ based Arduino IDE version 2.3.10

VegasEat  02oct2026
*/

unsigned long previousMillis = 0;
unsigned long interval = 500;  // Blink every 500 ms

void setup() {
  // initialize digital pin LED_BUILTIN (pin 13) as an output.
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  unsigned long currentMillis = millis();

  // Check if it's time to toggle the LED
  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;

    // Toggle/Flip LED state (! means not)
    digitalWrite(LED_BUILTIN, !digitalRead(LED_BUILTIN));
  }

  // Now non-blocking code can run here
}