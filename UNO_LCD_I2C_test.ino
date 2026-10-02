/* UNO_LCD_I2C_test.ino

Exploring an Arduino UNO programmable controller:
Testing a LCD 16x2 (I2C) Liquid Crystal display
(MCP23008 based, costs about $4)

Important:
Compiles, but characters don't show until the contrast potentiometer on
the backside of the LC display is properly adjusted!

https://docs.arduino.cc/libraries/liquidcrystal/

the display has 4 pins on the left section
(top to bottom)
1 ground
2 +5V      +3.3V too low
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
  lcd.print("UNO R4 WiFi!");
  lcd.write(123);       // ascii value of one character to show
  lcd.scrollDisplayLeft();  // whole display 1 space (loop it)
  lcd.scrollDisplayRight(); // dito
  lcd.display();
  lcd.createChar(index, byteArray[]) // form custom character

I am using the free C++ based Arduino IDE version 2.3.10
Install the needed header files with the IDE's Library Manager

VegasEat  02oct2026
*/

#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// create the class instance, call it lcd
LiquidCrystal_I2C lcd(0x27, 16, 2);  // 0x27 or maybe 0x3F

void setup() {
  // some required basic comands...
  lcd.init();
  // must turn on backlight
  lcd.backlight();
  // cursor to column, row
  lcd.setCursor(0, 0);
  // show some text, 16 characters max.
  lcd.print("PI Day ..............");
  // cursor to column, row
  lcd.setCursor(0, 1);
  lcd.print(3.14);
  lcd.print(" -- ");
  lcd.write(123);  // ascii for '{'
  lcd.write(125);  // ascii for '}'
}

void loop() {
  // not used this time
}
