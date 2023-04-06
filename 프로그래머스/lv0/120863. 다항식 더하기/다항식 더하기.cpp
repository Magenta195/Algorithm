#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

string solution(string polynomial) {
    map<string, int> poly_result = {
        {"x", 0},
        {"" , 0}
    };
    string answer = "";
    string typ = "";
    int num = 0, cnt = 0;
        
    for (const auto p : polynomial) {
        if ( p == ' ')
            continue;
        if ( p == '+' ) {
            poly_result[typ] += (cnt == 0 ) ? 1 : num;
            num = 0;
            cnt = 0;
            typ = "";
        }
        else if ( p == 'x') {
            typ = "x";
        }
        else {
            cnt++;
            num = 10 * num + int( p - '0' );
        }
    }
    poly_result[typ] += (cnt == 0 ) ? 1 : num;
    
    if (poly_result["x"] > 0 && poly_result[""] > 0) {
        answer += (poly_result["x"] == 1)? "" : to_string(poly_result["x"]);
        answer += "x + ";
        answer += to_string(poly_result[""]);
    }
    else if (poly_result["x"] > 0) {
        answer += (poly_result["x"] == 1)? "" : to_string(poly_result["x"]);
        answer += "x";
    }
    else if (poly_result[""] > 0)
        answer += to_string(poly_result[""]);
    else
        answer += "0";
        
    return answer;
}