/* UNO_LCD_I2C_counter.ino

Exploring an Arduino UNO programmable controller:
Testing a LCD 16x2 (I2C) Liquid Crystal display
(MCP23008 based, costs about $4) counting seconds passed

Important:
Compiles, but characters don't show until the contrast potentiometer on
the backside of the LC display is properly adjusted!

https://docs.arduino.cc/libraries/liquidcrystal/

the display has 4 pins on the left section
(top to bottom)
1 ground
2 +5V      (+3.3V is too low)
3 signal SDA to arduino pin SDA or A4
4 signal SCL to arduino pin SCL or A5

  // all the official Liquid Crystal display commands...
  lcd.init();
  lcd.begin(16, 2);   // width, height in characters
  lcd.clear();
  lcd.home();         // default is col=0, row=0  (ULC)
  lcd.backlight();    // needs to be on, so call it  
  lcd.cursor();
  lcd.noCursor();
  lcd.blink();        // cursor position blinks
  lcd.noBlink();
  lcd.setCursor(col, row)  // zero based
  lcd.autoscroll(); 
  lcd.noAutoscroll();
  lcd.leftToRight();    // default
  lcd.rightToLeft();
  lcd.print("UNO R4 WiFi!");  // text or number
  lcd.write(123);             // ascii value of one character to show
  lcd.scrollDisplayLeft();    // whole display 1 space (loop it)
  lcd.scrollDisplayRight();   // dito
  lcd.display();
  lcd.createChar(index, byteArray[]) // form custom character

I am using the free C++ based Arduino IDE version 2.3.10
If you get a missing header error...
Install the needed header file with the IDE's Library Manager

If you get a "can't find port error", simply unplug and replug USB

VegasEat  02oct2026
*/

#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// create the class instance, let's 'call it lcd
LiquidCrystal_I2C lcd(0x27, 16, 2);  // 0x27 or maybe 0x3F

unsigned long seconds = 0;

void setup() {
  // required
  lcd.init();
  // must turn on backlight
  lcd.backlight();
  // show some text
  // column = 0, row = 0 by default
  lcd.print("Count seconds:");
}

void loop() {
  // column = 0, row = 1
  lcd.setCursor(0, 1);
  lcd.print(seconds);
  delay(1000);  // delay 1000 ms or 1 second
  seconds += 1;
}
