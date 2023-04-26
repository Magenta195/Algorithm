#include <string>
#include <vector>

using namespace std;

int solution(int number, int n, int m) {
    if (number % n)
        return 0;
    if (number % m)
        return 0;
    return 1;
}