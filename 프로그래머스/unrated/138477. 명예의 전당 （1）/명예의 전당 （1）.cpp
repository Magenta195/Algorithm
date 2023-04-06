#include <string>
#include <vector>
#include <queue>

using namespace std;

vector<int> solution(int k, vector<int> score) {
    priority_queue<int> pq;
    vector<int> answer;
    
    for (const auto s : score) {
        pq.push(-s);
        if (pq.size() > k)
            pq.pop();
        answer.push_back(-1 * pq.top());
    }
    
    return answer;
}