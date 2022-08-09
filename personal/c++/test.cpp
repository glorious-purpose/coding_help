#include <iostream>
#include <vector>

using namespace std;

int main(){
  vector<int> v = {1,2,3,4,5};
  v[3] = 10;
  for (int i = 0; i < v.size(); i++){
    cout << v[i] << " ";
  }
  v.erase(v.begin()+2);
  cout << endl;
  for (int i = 0; i < v.size(); i++){
    cout << v[i] << " ";
  }
  cout << endl;
  return EXIT_SUCCESS;
}
