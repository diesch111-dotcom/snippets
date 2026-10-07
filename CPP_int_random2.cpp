/* CPP_int_random2.cpp

pick random integers from  a given range

VegasEat   05oct2026
*/

#include <iostream>
#include <random>

int main() {
	std::random_device rd;   // Hardware seed source
	std::mt19937 gen(rd());  // Generator engine is a Mercine Twister
	std::uniform_int_distribution<int> dist(0, 255); // Range [0, 255]

	std::cout << dist(gen) << ", ";
	std::cout << dist(gen) << ", ";
	std::cout << dist(gen) << '\n';

	// potential output: 27, 2, 148

	return 0;
}

