/* CPP_int_random.cpp

generate random integers within a range

VegasEat   05oct2026
*/

#include <iostream>
#include <random>

int main() {
    // 1. Seed the engine using a non-deterministic hardware source if available
    std::random_device rd;
    
    // 2. Initialize the Mersenne Twister engine with the random seed
    // use std::mt19937_64 for 64-bit bounds
    std::mt19937 gen(rd());
    
    // 3. Define the desired range and distribution [min, max]
    std::uniform_int_distribution<int> distrib(1, 255); 

    // Generate random numbers
    for (int i = 0; i < 10; ++i) {
        std::cout << distrib(gen) << " ";
    }
    // potential output: 176 26 239 91 171 95 189 9 164 185
    
    return 0;
}
