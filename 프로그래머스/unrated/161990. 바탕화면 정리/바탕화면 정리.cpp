#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<string> wallpaper) {
    int lux = 51, luy = 51, rdx = 0, rdy = 0;
        
    for (int i = 0 ; i < wallpaper.size() ; i++ ){
        for (int j = 0 ; j < wallpaper[0].size() ; j++) {
            if (wallpaper[i][j] == '#') {
                lux = min(lux, j);
                luy = min(luy, i);
                rdx = max(rdx, j+1);
                rdy = max(rdy, i+1);
            } 
        }
    }
    vector<int> answer = {luy, lux, rdy, rdx};
    return answer;
}