#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> numbers) {
    sort(numbers.begin(), numbers.end());
    
    if (numbers.size() == 2) 
        return numbers[0] * numbers[1];
    
    vector<int>::iterator start = numbers.begin(), end = numbers.end();
    return max((*start)*(*(start+1)), (*(end-1))*(*(end-2)));
}