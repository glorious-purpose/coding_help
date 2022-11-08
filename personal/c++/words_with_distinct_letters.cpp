#include <iostream>
#include <vector>
#include <string>
#include <bitset>


int main(){
  std::string word = "Hello";
  unsigned int r = 0;

  for(char c: word){
    r |= 1 <<(c-'a');
    std::bitset<26> x(r);
    std::cout << x << ": " << x.count() << '\n';
  }
  std::bitset<26> x(r);
  std::cout << x << ": " << x.count() << std::endl;
  return EXIT_SUCCESS;
};
