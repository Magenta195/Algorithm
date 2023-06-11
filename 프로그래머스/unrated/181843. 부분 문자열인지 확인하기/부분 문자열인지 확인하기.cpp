#include <string>
#include <vector>

using namespace std;

int solution(string my_string, string target) {
    if (my_string.size() < target.size())
        return 0;
    
    for (int i = 0; i < my_string.size() - target.size()+1; i++) {
        if (target == my_string.substr(i, target.size()))
            return 1;
    }
    return 0;
}