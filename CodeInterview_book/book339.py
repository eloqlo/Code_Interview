import sys

def solution():
    n, m, k_dist, x = map(int, sys.stdin.readline().split())
    # N개 도시
    # M개 도로
    # K 거리인
    # X로 부터

    # O(1,000,000)
    d ={}
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        if a in d:
            d[a].add(b)
        else:
            d[a] = set([b])

    cur = [x]
    cur_dist = 0
    visit = set([x])
    while cur:
        cur_dist += 1
        nxt = []
        for node in cur:
            if node not in d:
                continue                        # 연결 노드 없는 끝 노드
            for nxt_node in d[node]:
                if nxt_node in visit:
                    continue                    # 앞서 방문했던 노드는 최단거리가 아니므로 계산서 제외
                visit.add(nxt_node)
                nxt.append(nxt_node)
        if cur_dist == k_dist:
            if nxt:
                return nxt
            else:
                return [-1]
        cur = nxt
    
    return [-1]

if __name__ == "__main__":
    result = solution()
    result.sort()
    for foo in result:
        print(foo)
    #END