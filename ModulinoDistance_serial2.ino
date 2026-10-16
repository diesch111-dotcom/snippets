/* ModulinoDistance_serial2.ino

'ModulinoDistance' measures distance using an infrared laser and 
Time-of-Flight technology detecting the time it takes for the IR beam 
to reflect back from a reflective object (avoid dull black)  It is one 
of the plug and make Modulino boards recognizable by a ruler symbol.
 
Sensor specifications:
Measurement range: Typically 0 mm to 4000 mm (4 meters)
Accuracy: 3% of distance
Measurement unit: Millimeters (mm)

info
https://github.com/arduino-libraries/Arduino_Modulino/tree/main/examples/Modulino_Distance

I am using the C++ based Arduino IDE version 2.3.10

VegasEat  15oct2026
*/

#include <Arduino_Modulino.h>

// Create a ModulinoDistance object
ModulinoDistance distance;

void setup() {
  // the required begin() methods
  Serial.begin(9600);  // show our results...
  Modulino.begin();
  distance.begin();
}

void loop() {
  // Hold a solid object in front of the module 
  // (has a narrow cone of detection)
  // Check if new distance measurement is available
  // This ensures we only read when fresh data comes in
  if (distance.available()) {
    // Get the latest distance measurement in millimeters (mm)
    // Values typically range from 0 mm to 4000 mm
    int measure_mm = distance.get();
    int measure_cm = measure_mm/10;
    Serial.print(measure_mm);
    Serial.print(" mm   ");
    Serial.print(measure_cm);
    Serial.println(" cm");
  }
  // Small millisecond delay to steady Serial Monitor readability
  delay(100);
}
