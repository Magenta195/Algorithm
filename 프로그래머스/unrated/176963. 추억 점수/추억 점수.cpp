#include <string>
#include <vector>
#include <map>

using namespace std;

vector<int> solution(vector<string> name, vector<int> yearning, vector<vector<string>> photo) {
    map<string, int> name_map;
    vector<int> answer;
    for (int i = 0 ; i < name.size() ; i++ ) {
        name_map.insert({name[i], yearning[i]});
    }
    
    for (const auto _photo : photo) {
        int sum = 0;
        for (const auto people : _photo) {
            if (name_map.find(people) != name_map.end())
                sum += name_map[people];
        }
        answer.push_back(sum);
    }
    
    return answer;
}