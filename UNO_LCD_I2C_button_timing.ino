/* UNO_LCD_I2C_button_timing.ino
 
 Measure the time a button is pressed in milliseconds,
 show duration using a LCD 16x2 (I2C) Liquid Crystal display.
 Connnect a pushbutton (can be module) between GND and pin 7,
 keep this pin high using its internal pullup resistor
 
 Different durations can be used to trigger different actions.

 The display has 4 pins on the left section
 (top to bottom)
 1 ground
 2 +5V
 3 signal SDA to arduino pin SDA or A4
 4 signal SCL to arduino pin SCL or A5

VegasEat  16sep2026
*/

#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);  // 0x27 or maybe 0x3F

// use board's builtin LED = LED_BUILTIN
int led_pin = 13;
int button_pin = 7;
unsigned long duration;
// gets value from millis() when the switch is pressed
unsigned long startTime;

void setup() {
  // a pushbutton is connected to pin 7, this pin is set HIGH
  // using its internal pullup resistor, button-press will make it LOW
  pinMode(button_pin, INPUT_PULLUP);
  pinMode(LED_BUILTIN, OUTPUT);

  lcd.init();
  // must turn on backlight
  lcd.backlight();
  // show some text
  // column = 0, row = 0 by default
  lcd.print("Button pressed:");
}

void loop() {
  // check if button is pressed
  if (digitalRead(button_pin) == LOW) {
    startTime = millis();
    // turn on the LED
    digitalWrite(LED_BUILTIN, HIGH);
    // wait while the button is still pressed
    while (digitalRead(button_pin) == LOW)
      ;
    duration = millis() - startTime;

    // set the cursor to (column=0, row=1):
    lcd.setCursor(0, 1);
    lcd.print(duration);
    lcd.print(" millisec");
  }
  // turn off the LED
  digitalWrite(LED_BUILTIN, LOW);
}
