#include <string>
#include <vector>

using namespace std;

int solution(vector<string> s1, vector<string> s2) {
    int answer = 0;
    for (auto _s1 : s1) {
        for (auto _s2 : s2) {
            if (_s1 == _s2) answer++;
        }
    }
    return answer;
}