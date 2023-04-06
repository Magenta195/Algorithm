#include <string>
#include <vector>
#include <sstream>

using namespace std;

vector<string> split(string target, char s) {
    istringstream _target(target);  
    string buffer;           
    vector<string> splited;
    
    while (getline(_target, buffer, s)){
        splited.push_back(buffer);
    }
    return splited;
}

int solution(string s) {
    vector<string> s_vec = split(s, ' ');
    vector<int> stk;
    
    for (const auto _s_vec : s_vec ) {
        if ( _s_vec == "Z" )
            stk.pop_back();
        else 
            stk.push_back( stoi(_s_vec) );
    }
    
    int answer = 0;
    for (const auto num : stk ) {
        answer += num;
    }
    
    return answer;
}