#include <string>
#include <vector>

using namespace std;

vector<int> solution(int num, int total) {
    int result = (total - (num*num - num) / 2) / num;
    vector<int> answer;
    for (int i = 0; i < num; i++)
        answer.push_back(result+i);
    return answer;
}