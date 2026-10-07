/* UNO_OLED_milli_time.ino

Arduino + OLED display combo is one of the cleanest ways to show text, sensor data, or
graphics on your projects. The most common module is the 0.96" 128×64 SSD1306 I2C OLED,
which uses only four wires and works on both 3.3V and 5V.

 Has 4 pins (l to r):
  1 GND
  2 VCC  +5V
  3 SCL  I2C clock line to UNO pin A5 (use yellow jumber)
  4 SDA  I2C data line  to UNO pin A4

careful...
sometimes GND and +5V are reversed, should be marked
Typical I2C address: 0x3C (rarely 0x3D)

millis() uses unsigned long values
0 to 4,294,967,295 (2^32 - 1) or about 50 days in millisec
after that it will reset to zero and count up again

Install via Arduino IDE → Library Manager:
Adafruit SSD1306
Adafruit GFX      (for graphics comes along)

I am using the C++ based Arduino IDE version 2.3.10
Help/Reference brings up potential built-in C++ details

If port is not found unplug/replug USB

VegasEat  05oct2026
*/

#include <Wire.h>
//#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);

void setup() {
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
  //unsigned long currentMillis = millis();

  // millis() uses unsigned long values
  // 0 to 4,294,967,295 (2^32 - 1) or about 50 days in millisec
  // after that it will reset to zero and count up again
  display.setCursor(0, 0);  // ULC  column, row in pixels
  unsigned long millisec = millis();
  unsigned long sec = millisec/1000;
  unsigned long min = sec/60;
  unsigned long hr = min/60;

  display.print(millisec);
  display.setCursor(0, 16);
  display.print(sec);

  display.setCursor(0, 16*2);
  display.print(min);
  display.print(" m");

  display.setCursor(0, 16*3);
  display.print(hr);
  display.print(" h");  

  display.display();
  delay(1000);  // in milliseconds
  display.clearDisplay();
}

/*
  // displays 21 characters per text-line for TextSize(1)
  // total 8 text-lines/diplay panel each 8 pixels heigh
  // displays 10 characters per text-line for TextSize(2)
  // total 4 text_lines/display panel each 16 pixels heigh
  // excess text will wrap into next text-line
  display.setTextSize(2);
  display.setTextColor(WHITE);
  // top left setCursor(0, 0) column, row in pixels
  display.setCursor(0, 0);
  display.println("Hello OLED");

  display.setCursor(0, 18);
  display.println("Hello OLED");

  display.setTextSize(1);
  display.setCursor(0, 18*2);
  display.println("now use text size 1");

  float cost = 123.4567;
  display.setCursor(0, 18*2+10);
  // no new line char
  display.print("Cost = $");
  // round to 2 decimal
  display.println(cost, 2);

  display.display();

*/
