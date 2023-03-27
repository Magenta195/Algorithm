#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0;
    for (const auto s : to_string(n) )
        answer += s - '0';
    
    return answer;
}