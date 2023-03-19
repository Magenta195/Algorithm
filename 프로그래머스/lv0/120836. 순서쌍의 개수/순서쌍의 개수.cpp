#include <string>
#include <vector>
#include <cmath>

using namespace std;

int solution(int n) {
    int answer = 0;
    for (int i = 1 ; i <= sqrt(n) ; i++ ) answer += n % i ? 0 : ( i == n / i ? 1 : 2) ;
    return answer;
}