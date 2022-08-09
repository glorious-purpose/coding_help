#include <iostream>
#include <unordered_set>

using namespace std;

int txpone(long num, long &v, long orig_num) {
  v++;
  if (num < orig_num || num == 1 || num == 2 || num == 4) {
    return 1;
  }
  if (num % 2 == 0) {
    return txpone(num / 2, v, orig_num);
  } else {
    return txpone(num * 3 + 1, v, orig_num);
  }
}

int main() {
  long visited = 0;
  long numbers_to_eval = 1000000000;
  for (long i = 1; i <= numbers_to_eval; i++){
    txpone(i, visited, i);
  }
  cout << "Analyzing " << numbers_to_eval << " numbers visits " << visited << " numbers." << endl;
  return EXIT_SUCCESS;
}
