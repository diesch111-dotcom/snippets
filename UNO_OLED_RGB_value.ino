/* UNO_OLED_RGB_value.ino

RGB LED standalone is in a clear plastic dome housing with 4 leads:
red     (flat spot on plastic housing)
cathode (longest)
green
blue

Red source color Al-GaInP on GaAs substrate LED 650nm peak
Blue source color InGaN LED 468nm peak
Green source color InGaN on Sapphire LED 515nm peak
 
Insert the RGB LED into 4 adjoining analog inputs 
A0 red, A1 cathode, A2 green, A3 blue
then set A1 to Low (GND level) with pinMode(A1, OUTPUT) then digitalWrite(A1, LOW) and 
use red, green and blue LEDs as photo receivers via pinMode(color, INPUT) and 
int val = analogRead(color)

Arduino + OLED display combo is one of the cleanest ways to show text, sensor data, or
graphics on your projects. The most common module is the 0.96" 128×64 SSD1306 I2C OLED,
which uses only four wires and works on both 3.3V and 5V.

Has 4 pins (l to r):
  1 GND
  2 VCC  +5V
  3 SCL  I2C clock line to UNO pin A5 (use yellow jumber)
  4 SDA  I2C data line  to UNO pin A4

Install via Arduino IDE → Library Manager:
Adafruit SSD1306
Adafruit GFX     (for graphics comes along)

If port is not found unplug/replug USB

*/

#include <Wire.h>
//#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);

void setup() {
  pinMode(A0, INPUT);   // red
  pinMode(A1, OUTPUT);  // common cathode
  pinMode(A2, INPUT);   // green
  pinMode(A3, INPUT);   // blue
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);  // I2C address
  display.clearDisplay();
  // needed
  display.setTextColor(WHITE);
  // displays 10 characters per text-line for TextSize(2)
  // total 4 text_lines/display panel each 16 pixels heigh
  // displays 21 characters per text-line for TextSize(1)
  // total 8 text-lines/diplay panel each 8 pixels heigh
  display.setTextSize(2);
}

void loop() {
  int red = analogRead(A0);
  int green = analogRead(A2);
  int blue = analogRead(A3);

  display.setCursor(0, 16);
  display.print(red);
  display.print(" R");

  display.setCursor(0, 16 * 2);
  display.print(green);
  display.print(" G");

  display.setCursor(0, 16 * 3);
  display.print(blue);
  display.print(" B");

  display.display();
  delay(1000);  // in milliseconds
  display.clearDisplay();
}
