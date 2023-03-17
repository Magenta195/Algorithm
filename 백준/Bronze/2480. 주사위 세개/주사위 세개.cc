#include <iostream>

int main() {
    int a, b, c, cnt;
    std::cin >> a >> b >> c;

    if (a == b && b == c) {
      std::cout << 10000 + 1000*a << std::endl;
    }
    else if (a == b || b == c || c == a) {
      std::cout << 1000 + 100 * (( a == b ) ? a : c) << std::endl;
    }
    else {
      std::cout << 100*std::max(a, std::max(b, c)) << std::endl;
    }
}