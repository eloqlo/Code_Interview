#include <iostream>
#include <vector>
#include <deque>
#include <set>

using namespace std;

int main(void) 
{
    ios::sync_with_stdio(false);
    cout.tie(NULL);

    int N,M,tmp1,tmp2;
    cin >> N >> M;
    vector<set<int>> graph;
    vector<int> visit;
    for (int i=0; i<N+1; i++)
    {
        set<int> s;
        graph.push_back(s);
        visit.push_back(0);
    }
    for (int i=0; i<M; i++)
    {
        cin >> tmp1 >> tmp2;
        graph[tmp1].insert(tmp2);
        graph[tmp2].insert(tmp1);
    }
    
    // BFS
    int COUNT = 0;
    for (int node=1; node<N+1; node++)
    {
        if (visit[node]==1)
            continue;
        visit[node] = 1;
        COUNT += 1;
        
        deque<int> cur = {node};
        while (cur.size()>0)
        {
            int cur_node = cur[0];
            cur.pop_front();
            for (auto itor = graph[cur_node].begin(); itor!=graph[cur_node].end(); itor++)
            {
                if (visit[*itor] != 1)
                {
                    cur.push_back(*itor);
                    visit[*itor] = 1;
                }
            }
        }//while
    }//for
    cout << COUNT;
    return 0;
}   //main