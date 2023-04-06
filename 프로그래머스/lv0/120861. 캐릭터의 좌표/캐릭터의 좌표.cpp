#include <string>
#include <vector>
#include <map>
#include <cmath>

using namespace std;

map<string, vector<int>> move_map = {
    {"up", {0, 1}},
    {"down", {0, -1}},
    {"left", {-1, 0}},
    {"right", {1, 0}}
};

vector<int> move(vector<int> board, vector<int> coord, vector<int> moved) {
    vector<int> moved_coord(coord);
    for (int i = 0 ; i < 2 ; i++ ) {
        moved_coord[i] += moved[i];
        if ( abs(moved_coord[i]) > abs(board[i] / 2) )
            return coord;
    }
    return moved_coord;
}


vector<int> solution(vector<string> keyinput, vector<int> board) {
    vector<int> answer = {0, 0};
    
    for (const auto keys : keyinput) {
        answer = move(board, answer, move_map[keys]);
    }
    
    return answer;
}