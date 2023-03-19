#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> num_list) {
    int i = count_if(num_list.begin(), num_list.end(), [](int i) {
        return i % 2;
    });
    
    return vector<int> { (int)num_list.size()-i, i };
}