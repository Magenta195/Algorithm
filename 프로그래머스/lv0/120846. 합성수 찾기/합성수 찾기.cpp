#include <string>
#include <vector>
#include <cmath>
using namespace std;

int solution(int n) {
    int answer = 0;
    bool flg;
    
    for (int i = 1; i <= n; i++) {
        if (i < 4)
            continue;
        flg = false;
        for (int j = 2; j <= sqrt(i) + 1; j++) {
            if ( i % j == 0 ) {
                flg = true;
                break;
            }
        }
        if (flg) 
            answer++;
    }
    
    return answer;
}