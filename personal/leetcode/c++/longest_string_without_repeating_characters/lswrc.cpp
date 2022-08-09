#include <string>
#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>

using namespace std;

class Solution {
public:
  int lswrc(string s) {
    if (s.length() < 2) {
      return s.length();
    }
    string longest_substring, current_substring;
    for (int i = 0; i < s.length(); i++){
      while (current_substring.find(s[i]) != current_substring.npos){
        current_substring.erase(0,1);
      }
      current_substring.append(s, i, 1);
      if (current_substring.length() > longest_substring.length()){
        longest_substring.assign(current_substring);
      }
    }
    return longest_substring.length();
  }
};

vector<string> get_problems_from_file(string fileName) {
  ifstream infile(fileName.c_str());
  if (!infile){
    cerr << "Cannot open file: " << fileName << endl;
    vector<string> vect;
    return vect;
  }
  string line;
  vector<string> problems;
  while (getline(infile, line)) {
    problems.push_back(line);
  }
  return problems;
}

vector<int> get_answers_from_file(string fileName) {
  ifstream infile(fileName.c_str());
  if (!infile){
    cerr << "Cannot open file: " << fileName << endl;
    vector<int> vect;
    return vect;
  }
  string line;
  vector<int> answers;
  while (getline(infile, line)) {
    stringstream lineStream(line);

    int value;
    while (lineStream >> value){
      answers.push_back(value);
    }
  }
  return answers;
}

int main(){
  Solution s;
  int result;
  vector<string> tests = get_problems_from_file("test/strings.txt");
  vector<int> answers = get_answers_from_file("test/answers.txt");
  for (int i=0; i<tests.size(); i++){
    result = s.lswrc(tests[i]);
    if (result == answers[i]){
      cout << "Match!\t";
    } else {
      cout << "\t";
    }
    cout << result << " -- " << answers[i] << "\n";
  }

  cout << endl;

  return EXIT_SUCCESS;
};
