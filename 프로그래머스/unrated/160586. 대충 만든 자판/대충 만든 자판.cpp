#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<string> keymap, vector<string> targets) {
    vector<int> answer;
    
    for ( const auto target : targets) {
        int key_val = 0;
        bool is_enable = true;
        
        for ( const auto t : target ) {
            int _key_val = 101;
            for ( const auto _keymap : keymap ){
                size_t idx = _keymap.find(t);
                if ( idx != string::npos )
                    _key_val = min(_key_val, int(idx)+1);
            }
            if (_key_val == 101){
                is_enable = false;
                break;
            }
            key_val += _key_val;
        }
        
        if (is_enable)
            answer.push_back(key_val);
        else
            answer.push_back(-1);
        
    }
    
    
    return answer;
}