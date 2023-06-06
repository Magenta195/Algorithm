#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> dx = {1, 0, -1, 0};
vector<int> dy = {0, 1, 0, -1};

vector<vector<int>> solution(int n) {
    vector<vector<int>> answer(n, vector<int>(n, 0));
    int x = 0, y = 0, dir = 0;
    for (int i = 1; i <= n*n; i++) {
        answer[y][x] = i;
        if ( x + dx[dir] < 0 || x + dx[dir] >= n ||
             y + dy[dir] < 0 || y + dy[dir] >= n ||
            answer[y + dy[dir]][x + dx[dir]] > 0)
            dir = ( dir + 1 ) % 4;
        x += dx[dir];
        y += dy[dir];
    }
    
    return answer;
}