#include <iostream>

int lcm(int a, int b) {
  if (b == 0) return a;
  return lcm(b, a%b);
}

int main() {
    int T, a, b;
    std::cin >> T;

    for (int i = 0; i < T; i++) {
      std::cin >> a >> b;
      std::cout << a*b / lcm(a, b) << std::endl;
    }
}