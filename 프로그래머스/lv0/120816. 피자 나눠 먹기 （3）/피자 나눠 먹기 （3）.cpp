#include <string>
#include <vector>

using namespace std;

int solution(int slice, int n) {
    return (n - 1) / slice + 1;
}