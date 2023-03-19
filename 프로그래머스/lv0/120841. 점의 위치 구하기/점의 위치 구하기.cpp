#include <string>
#include <vector>

using namespace std;

int solution(vector<int> dot) {
    if (dot[0] > 0) return dot[1] > 0 ? 1 : 4 ;
    return dot[1] > 0 ? 2 : 3 ;
}