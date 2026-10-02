/* UNO_LCD_I2C_voltages.ino

Exploring an Arduino UNO programmable controller:
Testing a LCD 16x2 (I2C) Liquid Crystal display
(MCP23008 based, costs about $4) measure 2 voltages
using 2 analog inputs and show the result on 2 separate 
rows of an LCD display.

The display has 4 pins on the left section
(top to bottom)
1 ground
2 +5V
3 signal SDA to arduino pin SDA or A4
4 signal SCL to arduino pin SCL or A5

The voltage source is the UNO +3.3V with two 10k ohm resistors
connected in series between GND and + forming a divider.
One voltage is read at +3.3V, the other from the center of 
the voltage divider, should be +1.65V depending on resistor tolerance

On the UNO max. voltage on the analog inputs is +5.5V
For higher DC voltages apply an appropriate voltage divider
and correct the value in the code.

I am using the free C++ based Arduino IDE version 2.3.10
If you get a missing header error...
Install the needed header file with the IDE's Library Manager

If you get a "can't find port error", simply unplug and replug USB

VegasEat  02oct2026
*/

#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// create the class instance, let's 'call it lcd
LiquidCrystal_I2C lcd(0x27, 16, 2);

// assign the analog pins
int voltPin1 = A0;  // center of voltage divider
int voltPin2 = A1;  // +3.3V from UNO

void setup() {
  // required
  lcd.init();
  // must turn on backlight
  lcd.backlight();
  pinMode(voltPin1, INPUT);
  pinMode(voltPin2, INPUT);
}

void loop() {
  // read the input on the specified Arduino analog pin
  int sensorValue1 = analogRead(voltPin1);
  int sensorValue2 = analogRead(voltPin2);
  // convert the 10bit analog reading which goes
  // from 0 to 1023 to a voltage 0 to 5V)
  float voltage1 = sensorValue1 * (5.0 / 1023.0);
  float voltage2 = sensorValue2 * (5.0 / 1023.0);

  // first row
  // set the cursor to (column=0, row=0):
  lcd.setCursor(0, 0);
  lcd.print(voltage1);
  lcd.print(" volts");
  // second row
  lcd.setCursor(0, 1);
  lcd.print(voltage2);
  lcd.print(" volts");
  // time to read result
  delay(3000);

  // clear screen for the next loop
  lcd.clear();
}
