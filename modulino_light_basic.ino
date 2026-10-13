/* modulino_light_basic.ino

The Modulino Light uses a simple circuit built around the LTR-381RGB-01 sensor (U1), 
which handles colour detection, ambient light measurement, and I²C communication.

update(): Updates sensor readings, returns true if successful
getColor(): Returns colour as ModulinoColor object (extract RGB with bit shifting)
getColorApproximate(): Returns colour name as String (e.g., "RED", "BLUE", "GREEN")
getAL(): Returns raw ambient light value
getLux(): Returns calibrated lux value
getIR(): Returns infrared level

https://docs.arduino.cc/tutorials/modulino-light/how-light/

VegasEat  13oct2026
*/

#include <Modulino.h>

ModulinoLight light;

void setup() {
  Serial.begin(9600);
  Modulino.begin();
  light.begin();
}

void loop() {
  // Update sensor readings
  light.update();
  
  // Get colour approximation
  String colourName = light.getColorApproximate();
  
  // Get RGB values
  ModulinoColor colour = light.getColor();
  int r = (0xFF000000 & colour) >> 24;
  int g = (0x00FF0000 & colour) >> 16;
  int b = (0x0000FF00 & colour) >> 8;
  
  // Get light intensity values
  int lux = light.getAL();              // Ambient light (raw)
  int luxCalibrated = light.getLux();   // Calibrated lux
  int ir = light.getIR();               // Infrared level
  
  // Display readings
  Serial.print("Colour: ");
  Serial.print(colourName);
  Serial.print("\tRGB: (");
  Serial.print(r);
  Serial.print(", ");
  Serial.print(g);
  Serial.print(", ");
  Serial.print(b);
  Serial.print(")\tLux: ");
  Serial.print(luxCalibrated);
  Serial.print("\tIR: ");
  Serial.println(ir);
  
  delay(500);
}
