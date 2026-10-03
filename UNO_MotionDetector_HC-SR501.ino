/* UNO_MotionDetector_HC-SR501.ino

  This small sensor is included in many sensor assortments, recognizable
  by its dome shaped white plastic Fresnel lens.  The board has a built-in
  integrated circuit that handles all the logic and timing.

  The SR501 PIR detects infrared changes and interprets the motion.
  The device requires a one minute warm-up time after power is connected.
  It will detect motion inside a 110 degree cone with a range of 
  3 to 7 meters.  Any motion turns the sensor signal +3.3V HIGH.

  The module has two orange trim pots, the right side trim pot adjusts the
  viewing distance.  Full clockwise is 3 meters, full counter-clockwise
  is 7 meters.  The left trim pot adjusts the time delay.  Full clockwise 
  is a 5 minute delay. Full counter-clockwise sets the delay to 3 seconds.

  There is also a yellow jumper on the far right side. Jumper to the front
  starts the time delay immediately upon motion detection, then blocks 
  any further detection. Jumper to the rear will start the time delay 
  every time motion is detected.

  On the back side are three pins (left to right viewed from top):
  1 GND
  2 signal (to an Arduino digital IO pin)
  3 +5V 

  Some PIR modules have wires included.
  Suggested wire colors GND(brown), signal(orange), +5V(red)

  VegasEat  18sep2026
*/

int ledPin = 13;  // LED_BUILTIN is LED on Pin 13 of Arduino
int pirPin = 7;   // HC-S501 signal to an Arduino digital IO pin
int pirStatus; 

void setup() {

  pinMode(ledPin, OUTPUT);
  pinMode(pirPin, INPUT);

  digitalWrite(ledPin, LOW);
}

void loop() {
  pirStatus = digitalRead(pirPin);
  // LED turns on whenever motion is detected
  digitalWrite(ledPin, pirValue);

  // or you can activate a buzzer or a 
  // relay module to turn on a light
}
