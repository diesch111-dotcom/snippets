/* ModulinoMovement_serial2.ino

'ModulinoMovement' reads motion data using its accelerometer and 
gyroscope edged in its silicon chip in the form of a tuning fork.  It is one 
of the plug and make Modulino boards recognizable by a space-arrows symbol.
 
Sensor capabilities:
Accelerometer: Measures linear acceleration in 3 axes (X, Y, Z)
(all influenced by Earth's gravity)
Values are in g-force (g = 9.8 m/s*s)
Typical range: -2g to +2g
Gyroscope: Measures rotational velocity around 3 axes (roll, pitch, yaw)
Values are in degrees per second (°/s)
Roll: Rotation around X-axis (tilting left/right)
Pitch: Rotation around Y-axis (tilting forward/backward)
Yaw: Rotation around Z-axis (spinning clockwise/counterclockwise)

Pick up the module and move it in different directions like a drone to test it.

https://github.com/arduino-libraries/Arduino_Modulino/tree/main/examples/Modulino_Movement

I am using the C++ based Arduino IDE version 2.3.10

VegasEat  16oct2026
*/

#include <Arduino_Modulino.h>

// Create a ModulinoMovement object
ModulinoMovement movement;


// Variables to store accelerometer readings (g-force)
float x, y, z;
// Variables to store gyroscope readings (degrees/second)
// Might be familiar with these terms working with Drones
float roll, pitch, yaw;

void setup() {
  // the required begin() methods
  // Serial Monitor will show results
  Serial.begin(9600);
  // Initialize Modulino I2C communication
  Modulino.begin();
  movement.begin();
}

void loop() {
  // Read new movement data from the sensor
  // Call this before reading individual values
  movement.update();

  // Get acceleration values (in g-force, where g ≈ 9.8 m/s*s)
  x = movement.getX();  // X-axis acceleration
  y = movement.getY();  // Y-axis acceleration
  z = movement.getZ();  // Z-axis acceleration ( ~1.0 when upright)
  
  // Get gyroscope values (in degrees per second)
  roll = movement.getRoll();   // Rotation around X-axis (left/right tilt)
  pitch = movement.getPitch(); // Rotation around Y-axis (forward/backward tilt)
  yaw = movement.getYaw();     // Rotation around Z-axis (spinning)

  // Print acceleration values with 3 decimal places
  Serial.print("Acc: ");
  Serial.print(x, 3);
  Serial.print(" x,  ");
  Serial.print(y, 3);
  Serial.print(" y,  ");
  Serial.print(z, 3);
  Serial.print(" z ");
  
  // Separate Acceleration and Gyroscope values
  Serial.print(" |  Gyr: ");
  
  // Print gyroscope values with 1 decimal place
  Serial.print(roll, 1);
  Serial.print(" Roll,  ");
  Serial.print(pitch, 1);
  Serial.print(" Pitch,  ");
  Serial.print(yaw, 1);
  Serial.println(" Yawl");  // flush
  
  // Delay to make serial output somewhat readable
  delay(2000);
}
