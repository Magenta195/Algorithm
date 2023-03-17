#include <iostream>

int main() {
    int K, N, M;

    std::cin >> K >> N >> M;
    std::cout << std::max(0, K*N - M) << std::endl;
}