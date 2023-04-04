#include <string>
#include <vector>
#include <map>
#include <tuple>
#include <sstream>
#include <iostream>
using namespace std;
map<char, vector<int>> move_map = {
    {'E', {0, 1}},
    {'W', {0, -1}},
    {'N', {-1, 0}},
    {'S', {1, 0}}
};

vector<int> find_start(vector<string> park) {
    for (int i = 0 ; i < park.size(); i++ ) {
        for (int j = 0 ; j < park[0].size(); j++ ) {
            if (park[i][j] == 'S') {
                return vector<int> {i, j};
            }
        }
    }
}

tuple<bool, int, int> is_moveable(vector<int> coord, vector<string> park, string route) {
    vector<int> _coord(coord);
    vector<int> park_size = {static_cast<int>(park.size()), static_cast<int>(park[0].size())};
    vector<int> move_dir(move_map[route[0]]);
    
    for (int i = 0 ; i < static_cast<int>(route[2]) - '0' ; i++ ) {
        for (int j = 0 ; j < 2 ; j++ ) {
            _coord[j] += move_dir[j];
            if ( _coord[j] < 0 || _coord[j] >= park_size[j] )
                return make_tuple(false, -1, -1); 
        }
        
        if ( park[_coord[0]][_coord[1]] == 'X' )
            return make_tuple(false, -1, -1);
    }
    return make_tuple(true, _coord[0], _coord[1]);
}

vector<int> solution(vector<string> park, vector<string> routes) {
    int col = park.size(), row = park[0].size();
    
    vector<int> coord = find_start(park);
    
    for (const auto route : routes) {
        tuple<bool, int, int> move_result = is_moveable(coord, park, route);
        if (!get<0>(move_result))
            continue;
        coord[0] = get<1>(move_result);
        coord[1] = get<2>(move_result);
    }
    
    return coord;
}