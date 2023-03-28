#include <string>
#include <vector>
#include <iostream>

using namespace std;

string solution(int age) {
    string answer = "";
    for (const auto s : to_string(age)) {
        answer += s - '0' + 'a';
    }
    return answer;
}