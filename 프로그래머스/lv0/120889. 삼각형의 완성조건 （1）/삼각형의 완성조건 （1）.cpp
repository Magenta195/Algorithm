#include <string>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

int solution(vector<int> sides) {
    return ( *max_element(sides.begin(), sides.end()) < accumulate(sides.begin(), sides.end(), 0) - *max_element(sides.begin(), sides.end())) ? 1 : 2;
}