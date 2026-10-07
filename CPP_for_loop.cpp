/* CPP_for_loop.cpp

A close look at the for loop
btw:
Avoid putting leading zeros on decimal numbers they are used for octal numbers

VegasEat  07oct2026
*/

#include <iostream>
#include <vector>

int main() {
	std::vector<int> numbers = {10, 20, 30, 40};

	// iterate from k = 0 to k < 5 in steps 1
	// Initialization; Condition; Update
	for (int k = 0; k < 5; ++k) {
		std::cout  << k << "  ";
	}
	// outPut: 0  1  2  3  4

	std::cout << "\n";  // new line

	// Use const auto& to avoid copying elements
	for (const auto& num : numbers) {
		std::cout << num << " ";
	}
	// output: 10 20 30 40

	std::cout << "\n";  // new line

	// Use auto& to modify elements in place
	for (auto& num : numbers) {
		num *= 2;
		std::cout << num << " ";
	}
	// output: 20 40 60 80

	std::cout << "\n";  // new line

	// use Control Statements like continue or break
	for (int k = 1; k <= 8; ++k) {
		if (k == 3) continue;   // Skip 5
		if (k == 7) break;      // Exit loop before 7
		std::cout << k << " ";
	}
	// output: 1 2 4 5 6

	std::cout << "\n";  // new line

	for (int k = 0; k < 26; k = k + 5) {
		std::cout << std::dec << k << " octal = " << std::oct << k  << "\n";
	}
	/* output:
	0 octal = 0
	5 octal = 5
	10 octal = 12
	15 octal = 17
	20 octal = 24
	25 octal = 31
	*/
	
	// octal characters prefixed by a backslash
	std::cout << "\110\145\154\154\157\n";  // Hello
	// hexadecimal numbers are prefixed with \x
	std::cout << "\x48\x65\x6C\x6C\x6F\n"; //  Hello
	
	return 0;
}
