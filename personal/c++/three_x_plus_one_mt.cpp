// This is currently not working. Still figuring out multithreading.

#include <iostream>
#include <future>
#include <deque>
#include <vector>
#include <chrono>


using namespace std;

static int txpone(long num, long orig_num, long v = 0) {
  v++;
  if (num < orig_num || num == 1 || num == 2 || num == 4) {
    return v;
  }
  if (num % 2 == 0) {
    return txpone(num / 2, orig_num, v);
  } else {
    return txpone(num * 3 + 1, orig_num, v);
  }
}



int main() {
  long visited = 0;
  long numbers_to_eval = 1000;
  long num = 1;
  int thread_count = 8;
  vector<future<int>> threads;

  // Cycle through threads, adding new ones and removing joinable ones.
  while (num < numbers_to_eval || threads.size() > 0) {
    // add new threads up to thread_count
    while (threads.size() < thread_count && num < numbers_to_eval) {
      future<int> new_task = async(launch::async, txpone, num, num)
      threads.push_back(move(new_task));
      num++;
    }

    // join joinables and remove from threads.
    for (int i = thread_count - 1; i >= 0; i--){
      if (threads[i].wait_for(chrono::seconds(0)) == future_status::ready){
        visited += threads[i].get();
        threads.erase(threads.begin()+i);
      }
    }
  }
  cout << "Analyzing " << numbers_to_eval << " numbers visits " << visited << " numbers." << endl;
  return EXIT_SUCCESS;
}
