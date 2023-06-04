#include <string>
#include <vector>

using namespace std;

int solution(vector<int> num_list) {
    int mul = 1, sr = 0;
    for (const auto num : num_list) {
        mul *= num;
        sr += num;
    }
    sr *= sr;
    return mul < sr ? 1 : 0;
}