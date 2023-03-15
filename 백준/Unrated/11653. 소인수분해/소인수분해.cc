#include <iostream>

int main() {
    int i;
    std::cin >> i;

    while (i > 1) {
      int j = 2; 
      while (i % j) j += 1;
      std::cout << j << std::endl;
      i /= j;
    }
      
    return 0;
}