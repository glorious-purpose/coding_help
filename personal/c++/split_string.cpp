    #include <iostream>
    #include <algorithm>

    using namespace std;

    int main() {
      string text = "The dog walked in the park";
      string delim = " ";
      int delim_count = count(text.begin(), text.end(), ' ');
      string words[delim_count+1];
      size_t pos = 0;
      for (int i = 0; i <= delim_count; i++){
        pos = text.find(delim);
        words[i] = text.substr(0, pos);
        text.erase(0, pos+ delim.length());
      }
      for (int i = 0; i <= delim_count; i++){
        cout << "Word " << i+1 << ": " + words[i] << endl;
      }
      return EXIT_SUCCESS;
    }
