#include <iostream>
#include <string>
#include <iomanip>

int main() {
    double T, n;
    std::string str;

    std::cin >> T;
    std::cout << std::fixed;
    std::cout.precision(2);
    for (int i=0 ; i<T ; i++) {
      std::cin >> n;
      getline(std::cin, str);

      for (auto s : str) {
        if (s == '@') n *= 3.0;
        else if (s == '%') n += 5.0;
        else if (s == '#') n -= 7.0;
      }

      std::cout << n << std::endl;
    }

    return 0;
}