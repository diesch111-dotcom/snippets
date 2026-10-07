/* CPP_for_loop.ino

test the cpp for joop

int i = 255;
Serial.print(i, DEC); // Decimal (default): "255"
Serial.print(i, HEX); // Hexadecimal: "FF"
Serial.print(i, OCT); // Octal: "377"
Serial.print(i, BIN); // Binary: "11111111"

float i = 3.1415926;
Serial.print(i, 2); // Outputs: "3.14"
Serial.print(i, 4); // Outputs: "3.1416"

Serial.write(65);   // Prints "A" (ASCII 65 = 'A')

// Serial.write(buf, len)
byte data[] = {0x41, 0x42, 0x43}; // Raw bytes for 'A', 'B', 'C'
Serial.print(data[0]);    // Outputs: "65"
Serial.write(data, 3);    // Outputs: "ABC"

VegasEat  04oct2026
*/

void setup() {
    Serial.begin(9600); // Initialize serial communication at 9600 baud
}

void loop() {
    for (int i = 0; i < 5; i++) {
        Serial.print("Value of i: ");
        Serial.print(i);
        // Add a newline at the end of each iteration to flush
        Serial.println(); 
        delay(500);
    }
}
