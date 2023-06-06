#include <string>
#include <vector>

using namespace std;

vector<int> di = {0, 1, 1, 1, 0, -1, -1, -1};
vector<int> dj = {-1, -1, 0, 1, 1, 1, 0, -1};

int solution(vector<vector<int>> board) {
    int answer = 0, n = board.size();
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (board[i][j] == 0) {
                bool flg = true;
                for (int k = 0; k < 8; k++) {
                    int ai = i + di[k], aj = j + dj[k];
                    if ( ai >= 0 && ai < n &&
                        aj >= 0 && aj < n &&
                        board[ai][aj] == 1 ) {
                        flg = false;
                        break;
                    }
                }
                if (flg) answer++;
            }
        }
    }
    return answer;
}