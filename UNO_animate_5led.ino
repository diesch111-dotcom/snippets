/* UNO_animate_5led.ino

  Exercise a bunch of Light Emitting Diodes (LED)

  One can use a LED without the current limiting resistor using an 
  Arduino PWM pin (the pin with the ~ tilde/squiggly marker set to 255/5 or less)
  LED cathode (short lead, next to the flat edge on the casing, to lowest potential)
  eg. 
  LED cathode to GND, or digital IO pin set LOW
  LED anode to limiting resistor 330 ohm, or PWM pin set to <= 255/5

  Add more LEDs, as long as the anode goes into a PWM pin set to <= 255/5
  (mostly cut and past)

  VegasEat  06oct2026
*/

int red_cathode = 7;   // short LED lead
int red_anode = 6;     // PWM ~6, long LED lead
int grn_cathode = 4;   // short
int grn_anode = 5;     // PWM ~5, long
int yel_cathode = 2;   // short
int yel_anode = 3;     // PWM ~3, long
int blu_cathode = 8;   // short
int blu_anode = 9;     // PWM ~9, long
int wht_cathode = 12;  // short
int wht_anode = 11;    // PWM ~11, long

int pwm_level = 255 / 5;  // or less to be safe
int pwm_level2 = 0;       // off
int wait = 200;           // milliseconds

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);  // the onboard LED (pin 13)

  pinMode(red_cathode, OUTPUT);    // use digitalWrite
  digitalWrite(red_cathode, LOW);  // mimics GND, convenient location
  pinMode(red_anode, OUTPUT);      // will use analogWrite in loop()

  pinMode(grn_cathode, OUTPUT);    // use digitalWrite
  digitalWrite(grn_cathode, LOW);  // mimics GND, convenient location
  pinMode(grn_anode, OUTPUT);      // will use analogWrite in loop()

  pinMode(yel_cathode, OUTPUT);    // use digitalWrite
  digitalWrite(yel_cathode, LOW);  // mimics GND, convenient location
  pinMode(yel_anode, OUTPUT);      // will use analogWrite in loop()

  pinMode(blu_cathode, OUTPUT);    // use digitalWrite
  digitalWrite(blu_cathode, LOW);  // mimics GND, convenient location
  pinMode(blu_anode, OUTPUT);      // will use analogWrite in loop()

  pinMode(wht_cathode, OUTPUT);    // use digitalWrite
  digitalWrite(wht_cathode, LOW);  // mimics GND, convenient location
  pinMode(wht_anode, OUTPUT);      // will use analogWrite in loop()
}

// loop() is a while (true) loop ...
void loop() {
  // gradually turn all LEDs on
  analogWrite(wht_anode, pwm_level);
  delay(wait);
  analogWrite(blu_anode, pwm_level);
  delay(wait);
  analogWrite(red_anode, pwm_level);
  delay(wait);
  analogWrite(grn_anode, pwm_level);
  delay(wait);
  analogWrite(yel_anode, pwm_level);
  delay(wait);
  delay(1000);  // extra
  // gradually turn LEDs off
  analogWrite(wht_anode, pwm_level2);
  delay(wait);
  analogWrite(blu_anode, pwm_level2);
  delay(wait);
  analogWrite(red_anode, pwm_level2);
  delay(wait);
  analogWrite(grn_anode, pwm_level2);
  delay(wait);
  analogWrite(yel_anode, pwm_level2);
  delay(wait);
}
