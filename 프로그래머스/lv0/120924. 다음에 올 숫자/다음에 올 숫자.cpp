#include <string>
#include <vector>

using namespace std;

int solution(vector<int> common) {
    int result1 = common.back();
    common.pop_back();
    int result2 = common.back();
    common.pop_back();
    int result3 = common.back();
    if (result1 + result3 == result2 * 2)
        return result1*2 - result2;
    return result1*result1 / result2;
}