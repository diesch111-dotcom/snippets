/* CPP_binary.cpp

A look at C++ binary numbers/strings

VegasEat  07oct2026
*/

#include <iostream>
#include <bitset>
#include <string>

int main() {
	int x = 0b1010;
	int y = 0b11110000;
	int z = 0b11111111;
	// binary number represented as a string
	std::string binary_str = "1101";

	std::cout << x << "\n";  // Outputs: 10
	std::cout << y << "\n";  // Outputs: 240
	std::cout << z << "\n";  // Outputs: 255

	// convert the binary string to a 8-bit binary, then to a decimal
	std::bitset<8> bits(binary_str);
	unsigned long decimal_val = bits.to_ulong();
	std::cout << decimal_val << "\n";  // Outputs: 13

	for (int k = 0; k < 16; k++ ) {
		// show k as a 4-bit binary representation
		std::cout << k << " = " << std::bitset<4>(k) << "\n";
	}
	/*
	0 = 0000
	1 = 0001
	2 = 0010
	3 = 0011
	4 = 0100
	5 = 0101
	6 = 0110
	7 = 0111
	8 = 1000
	9 = 1001
	10 = 1010
	11 = 1011
	12 = 1100
	13 = 1101
	14 = 1110
	15 = 1111
	*/

	// octal characters prefixed by a backslash
	std::cout << "\110\145\154\154\157\n";  // Hello
	// hexadecimal numbers are prefixed with \x
	std::cout << "\x48\x65\x6C\x6C\x6F\n"; //  Hello
}

