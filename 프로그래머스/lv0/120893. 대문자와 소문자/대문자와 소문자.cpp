#include <string>
#include <vector>

using namespace std;

string solution(string my_string) {
    string answer = "";
    for (const auto s : my_string)
        if (isupper(s)) answer += tolower(s);
        else answer += toupper(s);
    return answer;
}