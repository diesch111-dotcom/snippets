/* CPP_vector_test.cpp

std::vector is a dynamic array provided by the Standard
Template Library (<vector>). Unlike static arrays like
eg. int arr[10], vectors can grow and shrink dynamically
at runtime while storing contiguous elements in memory.

size(): Number of elements currently in the vector.

capacity(): Total elements the vector can hold before reallocating memory.

reserve(n): Allocates memory ahead of time to avoid multiple costly
  reallocations when growing a vector.

std::find performs a linear search ($O(n)$ time) across a range and
  returns an iterator to the first matching element, or vec.end() if not found.

std::sort typically uses IntroSort (a hybrid of QuickSort, HeapSort, and
  InsertionSort)


*/

#include <iostream>
#include <vector>
#include <algorithm>  // std::find  std::sort

int main() {
	std::vector<int> e_numbers;               // Empty vector
	std::vector<int> filled(5, 100);          // Size 5, all values set to 100
	std::vector<int> initialized = {1, 2, 3}; // Initializer list
	std::vector<int> numbers = {42, 12, 88, 3, 27};
	std::vector<int> numbers2 = {10, 20, 30, 20, 40};
	std::vector<int> numbers3 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
	std::vector<int> vec;

	// Adding and Removing Elements...
	// Adds 10 to the end
	vec.push_back(10);
	// Adds val20 to the end
	vec.push_back(20);
	// Adds 30 to the end
	vec.push_back(30);
	// Constructs element in-place (more efficient for objects)
	vec.emplace_back(77);
	// Removes the last element
	vec.pop_back();
	// Fast, no bounds checking
	int val1 = vec[0];
	// Safe: throws std::out_of_range if index is invalid
	int val2 = vec.at(1);

	// Returns first element
	int first = vec.front();
	// Returns last element
	int last = vec.back();

	// Range-based for loop (Recommended)
	for (int num : vec) {
		std::cout << num << " ";

	}
	// output: 10 20 30
	std::cout << "\n";  // new line
	std::cout << "size = " << vec.size() << "\n";          // 3
	std::cout << "capacity = " << vec.capacity() << "\n";  // 4

	vec.reserve(100);
	std::cout << "capacity = " << vec.capacity() << "\n";  // 100

	// std::find
	int target = 20;
	auto it = std::find(vec.begin(), vec.end(), target);

	if (it != vec.end()) {
		std::cout << *it << " at index " << std::distance(vec.begin(), it) << "\n";
	} else {
		std::cout << target << " not found.\n";
	}

	// Default sorting (Ascending order)
	std::sort(numbers.begin(), numbers.end());
	// Vector is now: {3, 12, 27, 42, 88}

	// Descending order using std::greater<T>()
	std::sort(numbers.begin(), numbers.end(), std::greater<int>());
	// Vector is now: {88, 42, 27, 12, 3}

	// Custom sorting with a Lambda (e.g., sort by remainder when divided by 5)
	std::sort(numbers.begin(), numbers.end(), [](int a, int b) {
		return (a % 5) < (b % 5);
	});

	// Remove all odd numbers, where n % 2 != 0
	numbers3.erase(
	std::remove_if(numbers3.begin(), numbers3.end(), [](int n) {
		return n % 2 != 0;
	}),
	numbers3.end()
	);
	// Range-based for loop (Recommended)
	for (int num : numbers3) {
		std::cout << num << " ";

	}
	// output: 2 4 6 8 10 
	std::cout << "\n";  // new line
}

