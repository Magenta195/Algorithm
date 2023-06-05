#include <string>
#include <vector>

using namespace std;

int solution(int a, int b) {
    if ( a % 2 > 0 && b % 2 > 0) 
        return a * a + b * b;
    if ( a % 2 > 0 || b % 2 > 0)
        return 2 * a + 2 * b;    
    return abs(a - b);
}