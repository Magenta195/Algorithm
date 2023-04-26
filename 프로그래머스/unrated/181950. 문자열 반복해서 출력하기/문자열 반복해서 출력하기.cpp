#include <iostream>
#include <string>

using namespace std;

int main(void) {
    string answer = "";
    string str;
    int n;
    cin >> str >> n;
    for (int i = 0; i < n; i++)
        answer += str;
    cout << answer << endl;
    return 0;
}