/* standard_stream_format.cpp

Standard stream-based formatting is safer than sprintf()

VegasEat  30sep2026
*/

#include <iostream>
#include <sstream>

int main() {
    std::ostringstream oss;
    int age = 77;
    float weight = 123.6;
    oss << "Age: " << age << ", Weight: " << weight;
    std::string result = oss.str();
    std::cout << result << "\n";
}
