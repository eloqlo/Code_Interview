// https://www.acmicpc.net/problem/11724

#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <stdlib.h>
#include <cstring>
#include <vector>
#include <algorithm>
#include <math.h>
#include <unordered_map>

using namespace std;

typedef struct {
    int num;
    int visited;
    vector<int> connected;
} node;

void dfs(node* nd, int num) {
    nd[num].visited = 1;
    for (int i = 0; i < nd[num].connected.size(); i++){
        if (nd[nd[num].connected[i]].visited == 0)
            dfs(nd, nd[num].connected[i]);
    }
}

int main(void) {
    int n,m;
    cin >> n >> m;
    node* nd = new node[n+1];       // node형 구조체 n+1개 heap에 할당받고, 주소를 넘김.

    // make graph
    for(int i=1; i<n+1; i++) {
        nd[i].num = i;
        nd[i].visited = 0;
    }       // 동적할당 받을 때, 배열은 초기화될 수 없다.
    int n1, n2;
    for(int i = 0; i < m; i++){
        cin >> n1 >> n2;
        nd[n1].connected.push_back(n2);
        nd[n2].connected.push_back(n1);
    }

    // travel graph
    int res = 0;
    for(int i=1; i < n+1; i++){
        if (nd[i].visited == 0) {
            dfs(nd, i);
            res++;
        }
    }
    cout << res << '\n';
    delete[] nd;        // 배열 크기 안써도 됨.

    return 0;
}