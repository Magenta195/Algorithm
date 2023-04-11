#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int i = 1;
    while (true) {
        if (i*6 >= n && i*6 % n == 0)
            return i;
        i++;
    }
}