/* UNO_blink_odd_even2.ino

  Exercise a bunch of Light Emitting Diodes (LED)

  One can use a LED without the current limiting resistor using an 
  Arduino PWM pin (the pin with the ~ tilde/squiggly marker set to 255/5 or less)
  LED cathode (short lead, next to the flat edge on the casing, to lowest potential)
  eg. 
  LED cathode to GND, or digital IO pin set LOW
  LED anode to limiting resistor 330 ohm, or PWM pin set to <= 255/5

  Add more LEDs, as long as the anode goes into a PWM pin set to <= 255/5

  VegasEat  06oct2026
*/

int led_cathode = 7;      // shorter LED lead
int led_anode = 6;        // PWM ~6, longer LED lead
int pwm_level = 255 / 5;  // or less to be safe

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);    // the onboard LED (pin 13)
  pinMode(led_cathode, OUTPUT);    // will use digitalWrite
  digitalWrite(led_cathode, LOW);  // mimics GND, convenient location
  pinMode(led_anode, OUTPUT);      // will use analogWrite
}

// a while (true) situation...
void loop() {
  unsigned long seconds = millis() / 1000;
  // when seconds value is even
  if (seconds % 2 == 0) {
    // blink the onboard LED too as an indicator
    digitalWrite(LED_BUILTIN, HIGH);
    analogWrite(led_anode, pwm_level);

  } else {
    digitalWrite(LED_BUILTIN, LOW);
    analogWrite(led_anode, LOW);
  }
}
