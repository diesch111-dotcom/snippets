/* CPP_sort_algorithm.cpp

The standard std::sort function sorts a range in ascending order by default. 
It uses 'Introsort', having a worst-case timing performance of O(N log N).

VegasEat  15oct2026
*/

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

int main() {
    std::vector<int> numbers = {4, 2, 5, 1, 3};
    std::vector<std::string> words = {"pear", "apple", "cherry", "quince"};
    
    // Sort in ascending order
    std::sort(numbers.begin(), numbers.end());

    for (int n : numbers) {
        std::cout << n << " "; // Output: 1 2 3 4 5
    }
    
    std::cout << "\n";  // new line

    // Descending order using std::greater
    std::sort(numbers.begin(), numbers.end(), std::greater<int>());   
 
     for (int n : numbers) {
        std::cout << n << " "; // Output: 5 4 3 2 1
    }
    
    std::cout << "\n";  // new line
    
    // Sort alphabetically (ascending) default
    std::sort(words.begin(), words.end());

    for (const std::string& w : words) {
        std::cout << w << " "; // Output: apple cherry pear quince 
    }      
    
    return 0;
}

