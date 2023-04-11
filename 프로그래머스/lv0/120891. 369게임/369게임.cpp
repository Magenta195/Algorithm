#include <string>
#include <vector>

using namespace std;

int solution(int order) {
    int answer = 0;
    for (const auto num : to_string(order)){
        if ( num == '3' || num == '6' || num == '9')
            answer++;
    }
    return answer;
}