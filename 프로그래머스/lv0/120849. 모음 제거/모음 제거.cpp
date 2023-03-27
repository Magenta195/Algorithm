#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(string my_string) {
    vector<char> vowels = {'a', 'e', 'i', 'o', 'u'};
    string answer = "";
    for (const auto s : my_string) {
        if (count(vowels.begin(), vowels.end(), s)) continue;
        answer += s;
    }
    return answer;
}