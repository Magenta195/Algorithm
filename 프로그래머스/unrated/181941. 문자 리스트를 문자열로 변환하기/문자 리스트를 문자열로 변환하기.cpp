#include <string>
#include <vector>

using namespace std;

string solution(vector<string> arr) {
    string answer = "";
    for (const auto str : arr)
        answer += str;
    return answer;
}