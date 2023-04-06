#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0, cnt = 0;
    while (cnt < n) {
        answer += 1;
        if (answer % 3 > 0 && to_string(answer).find('3') == string::npos )
            cnt += 1;
    }
    
    return answer;
}