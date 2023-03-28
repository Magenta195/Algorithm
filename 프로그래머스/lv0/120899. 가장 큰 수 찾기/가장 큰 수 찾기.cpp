#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> array) {
    int maxval = -1, maxidx = -1 ; 
    
    for (int i = 0; i < array.size() ; i++) {
        if (array[i] > maxval) {
            maxval = array[i];
            maxidx = i;
        }
    }
    
    return vector<int> {maxval, maxidx};
}