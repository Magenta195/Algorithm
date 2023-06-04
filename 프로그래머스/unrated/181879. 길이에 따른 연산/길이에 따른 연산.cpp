#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> num_list) {
    int answer = 0;
    if ( num_list.size() >= 11 ) {
        for (const auto num : num_list)
            answer += num;
    }
    else {
        answer = 1;
        for (const auto num : num_list)
            answer *= num;
    }
    return answer;
}