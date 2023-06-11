#include <string>
#include <vector>
#include <iostream>
using namespace std;

string solution(string myString) {
    string answer = "";
    for (const auto s : myString) {
        if (tolower(s) == 'a') {
            answer += toupper(s);
        }
        else {
            answer += tolower(s);
        }
    }
    return answer;
}