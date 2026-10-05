// C++ code
//
/* RGB_LED_random_blender2.ino.txt

  select the colors of the RGB LED at random
  
  the RGB LED has 4 leads (left to right):
  1 red lead (flat spot on plastic housing)
  2 cathode  (longeest lead)
  3 green lead
  4 blue lead
  (LED housing rim has flat portion near the red lead)

Red source color Al-GaInP on GaAs substrate LED 650nm peak
Blue source color InGaN LED 468nm peak
Green source color InGaN on Sapphire LED 515nm peak

Color mixing:
Red + Green = Yellow
Red + Blue = Purple/Magenta
Green + Blue = Cyan
All three = White
  
  blue lead via 220ohm resistor to an Arduino PWM pin
  green lead via 220ohm resistor to an Arduino PWM pin
  cathode (longer lead) connect to GND
  red lead via 220ohm resistor to an Arduino PWM pin
  
for buffer etc. see ...
https://www.tutorialspoint.com/c_standard_library/c_function_sprintf.htm
*/

// define Arduino pins used
#define BLUE 3   // UNO PMW pin ~3
#define GREEN 5  // UNO PMW pin ~5
#define RED 6    // UNO PMW pin ~6

// declare variables
int redValue;
int greenValue;
int blueValue;

// extra stuff
// give the character array buffer enough space
char buffer[35] = "";


void setup()
{
  Serial.begin(9600);
  // seed the random generator with the value of an unconnected pin
  int seedVal = analogRead(0);
  randomSeed(seedVal);
  Serial.println(seedVal);  // test
  
  // set pin modes
  pinMode(RED, OUTPUT);
  pinMode(GREEN, OUTPUT);
  pinMode(BLUE, OUTPUT);
  // set pin start conditions, start with RED
  digitalWrite(RED, HIGH);
  digitalWrite(GREEN, LOW);
  digitalWrite(BLUE, LOW);
}

// main loop
void loop()
{
  
  // choose a value between 0 and 255 at random
  redValue = random(0, 255);
  greenValue = random(0, 255);
  blueValue = random(0, 255);
 
  analogWrite(RED, redValue);
  analogWrite(GREEN, greenValue);
  analogWrite(BLUE, blueValue);
  
  // show the random color values
  sprintf(buffer, "red=%03d green=%03d blue=%03d ", 
    redValue, greenValue, blueValue);
  Serial.println(buffer);
    
  delay(3000);
}
  
