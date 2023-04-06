#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

map<string, int> player_map;
map<int, string> rank_map;

bool cmp(string a, string b) {
    return player_map[a] < player_map[b];    
}

vector<string> solution(vector<string> players, vector<string> callings) {
    int idx = 1;
    for (const auto player : players) {
        player_map[player] = idx;
        rank_map[idx] = player;
        idx++;
    }
    
    string player, front;
    int rank, front_rank;
    
    for (const auto calling : callings) {
        rank = player_map[calling];
        front_rank = rank-1;
        front = rank_map[front_rank];
        
        player_map[front] = rank;
        player_map[calling] = front_rank;
        rank_map[front_rank] = calling;
        rank_map[rank] = front;
        
    }
    
    sort(players.begin(), players.end(), cmp);
    return players;
}