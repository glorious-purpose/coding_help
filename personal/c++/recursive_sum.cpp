#include <iostream>
#include <iterator>
#include <ctime>
using namespace std;

// int sum_list_recursive(int* ptr, int array_size, int index = 0, int total = 0) {
//   if (index == array_size) {
//     return total;
//   }
//   return sum_list_recursive(ptr, array_size, index + 1, total + *(ptr + index));
// }

int sum_list_iterative(int* ptr, int array_size) {
  int total = 0;
  for (int i = 0; i < array_size; i++) {
    total = total + *(ptr + i);
  }
  return total;
}

int main() {
  int test_size = 10000;
  int test_list[test_size];
  srand(time(0));
  for(int i = 0; i < test_size; i++) {
    test_list[i] = 1 + 100.0 * (rand() / (RAND_MAX + 1.0));
  }
  // int n = sizeof(test_list)/sizeof(test_list[0]);
  // copy(test_list, test_list + n, ostream_iterator<int>(cout, "\n"));
  cout << "Total: " << sum_list_iterative(test_list, test_size) << endl;
  // cout << x << endl;
  return 0;
}
