#include <iostream>
#include <unordered_set>

using namespace std;

int txpone(int num, unordered_set<int> &v, int iter = 0) {
  if (v.count(num)) {
    return 1;
  }
  v.insert(num);
  if (num % 2 == 0) {
    return txpone(num / 2, v, iter + 1);
  } else {
    return txpone(num * 3 + 1, v, iter + 1);
  }
}

int main() {
  unordered_set<int> visited = {};
  int numbers_evaluated = 10000000;
  for (int i = 1; i <= numbers_evaluated; i++){
    if (!visited.count(i)){
      txpone(i, visited);
    }
  }
  cout << "Analyzing " << numbers_evaluated << " numbers visits " << visited.size() << " numbers." << endl;
  return EXIT_SUCCESS;
}
