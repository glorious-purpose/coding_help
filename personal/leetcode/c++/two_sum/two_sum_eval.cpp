// Solution from my leetcode submission for Two Sum in C++.
// Reads in values from files randomly generated using python.
// I'm attempting to determine what big O notation this provides by looking at N : time ratio.
// This is probably not the way to go about it, but there were a lot of things I had to learn to get this to work.
// - Reading from file.
// - Convert string of numbers to a vector<int>
// - Figure out how to time things, further learning on using (methods ? chrono::x)
// - Instantiating classes


#include <vector>
#include <chrono>
#include <iostream>
#include <algorithm>
#include <string>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <unordered_set>

using namespace std;


class Solution {
public:
  vector<int> twoSum(vector<int>& nums, int target) {
    int look_for;
    // Subtract each num from target and see if it is in vector.
    for (int i = 0; i < nums.size(); i++) {
      look_for = target - nums[i];
      vector<int>::iterator found_index = find(nums.begin() + i + 1, nums.end(), look_for);
      if (found_index != nums.end()) {
        int f = distance(nums.begin(), found_index);
        vector<int> x{i, f};
        return x;
      }
    }

    // No solution found
    vector<int> x{0, 0};
    return x;
  }

// Attempting to improve execution time using a set for answer lookup.
public:
  vector<int> twoSum_set(vector<int>& nums, int target) {
    int look_for;
    // Create set from vector.
    unordered_set<int> u_nums(nums.begin(), nums.end());

    // Subtract each num from target and see if it is in set.
    for (int i = 0; i < nums.size(); i++) {
      look_for = target - nums[i];
        if (u_nums.find(look_for) != u_nums.end()) {
          vector<int>::iterator found_index = find(nums.begin() + i + 1, nums.end(), look_for);
          if (found_index != nums.end()){
            int f = distance(nums.begin(), found_index);
            vector<int> x{i, f};
            return x;
          }
        }
    }

    // No solution found
    vector<int> x{0, 0};
    return x;
  }
};

vector<vector<int>> get_vectors_from_file(string fileName) {
  ifstream infile(fileName.c_str());
  if (!infile){
    cerr << "Cannot open file: " << fileName << endl;
    vector<vector<int>> vect;
    return vect;
  }
  string line;
  vector<vector<int>> vector_input;
  while (getline(infile, line)) {
    vector<int> v;
    stringstream lineStream(line);

    int value;
    while (lineStream >> value){
      v.push_back(value);
    }
    vector_input.push_back(v);
  }
  return vector_input;
}

vector<int> get_targets_from_file(string fileName) {
  ifstream infile(fileName.c_str());
  if (!infile){
    cerr << "Cannot open file: " << fileName << endl;
    vector<int> vect;
    return vect;
  }
  string line;
  vector<int> vector_input;
  while (getline(infile, line)) {
    stringstream lineStream(line);

    int value;
    while (lineStream >> value){
      vector_input.push_back(value);
    }
  }
  return vector_input;
}

// Found a guide online for beautifying output into columns
void print_menu(string iteration = "iter", string length = "n size", string result = "res", string time = "vector time", string res2 = "set res", string time2 = "set time") {
  cout << "|" << setw(4) << iteration
       << "|" << setw(10) << length
       << "|" << setw(10) << result
       << "|" << setw(10) << time
       << "|" << setw(10) << res2
       << "|" << setw(10) << time2
       << "|" << "\n";
}

int main(){
  Solution s;
  vector<vector<int>> test_vectors = get_vectors_from_file("test/vectors.txt");
  vector<int> test_targets = get_targets_from_file("test/targets.txt");
  vector<vector<int>> test_answers = get_vectors_from_file("test/answer.txt");
  // I need to learn how to throw exceptions... Until then, this verifies all files were read properly.
  if ((test_vectors.size() != test_targets.size()) || (test_targets.size() != test_answers.size())) {
    cerr << "Failed to open one or more files:" << "\n"
        << "Vectors: " << test_vectors.size() << "\n"
        << "Targets: " << test_targets.size() << "\n"
        << "Answers: " << test_answers.size() << endl;
    return EXIT_FAILURE;
  }

  // Once I have test values. Time function executiion and print out results.
  for (int i = 0; i < test_vectors.size(); i++) {
    // Get time of origianl function
    auto start = chrono::high_resolution_clock::now();
    vector<int> result = s.twoSum(test_vectors[i], test_targets[i]);
    auto stop = chrono::high_resolution_clock::now();
    string time1 = to_string(chrono::duration_cast<chrono::microseconds>(stop - start).count());

    // Sort results just in case. Pretty sure it will always be sorted regardless.
    sort(result.begin(), result.end());
    string success = "N";
    if (result == test_answers[i]){
      success = "Y";
    }

    // Get time of new function
    start = chrono::high_resolution_clock::now();
    result = s.twoSum_set(test_vectors[i], test_targets[i]);
    stop = chrono::high_resolution_clock::now();
    string time2 = to_string(chrono::duration_cast<chrono::microseconds>(stop - start).count());

    sort(result.begin(), result.end());
    string vsuccess = "N";
    if (result == test_answers[i]){
      vsuccess = "Y";
    }

    // Print results in columns
    print_menu(to_string(i+1), to_string(test_vectors[i].size()), success, time1, vsuccess, time2);
  }
  return EXIT_SUCCESS;
}
