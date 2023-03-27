#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 1;
    while (1) {
        if (answer * answer == n) return 1;
        if (answer * answer > n) return 2;
        answer++;
    }
}