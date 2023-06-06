#include <string>
#include <vector>

using namespace std;

bool isparallel(int x_diff1, int y_diff1, int x_diff2, int y_diff2) {
    return x_diff1 * y_diff2 == x_diff2 * y_diff1;
}

int solution(vector<vector<int>> dots) {
    if ( isparallel(dots[0][0]-dots[1][0], dots[0][1]-dots[1][1], dots[2][0]-dots[3][0], dots[2][1]-dots[3][1])
        || isparallel(dots[0][0]-dots[2][0], dots[0][1]-dots[2][1], dots[1][0]-dots[3][0], dots[1][1]-dots[3][1])
        || isparallel(dots[0][0]-dots[3][0], dots[0][1]-dots[3][1], dots[1][0]-dots[2][0], dots[1][1]-dots[2][1])
    )   return 1;
    return 0;
}