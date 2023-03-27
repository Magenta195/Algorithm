#include <string>
#include <vector>

using namespace std;

int solution(vector<int> array) {
    int answer = 0;
    
    for (auto num : array) {
        for (auto _num : to_string(num) ) {
            if (_num == '7') answer++;
        }
        
    }
    
    return answer;
}