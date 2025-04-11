dfs_counter = 0

def solution():
    N, M, V = map(int, input().split())
    d = {}
    for _ in range(M):
        a, b = map(int, input().split())
        if a in d:
            d[a].add(b)
        else:
            d[a] = set([b])
        if b in d:
            d[b].add(b)
        else:
            d[b] = set([a])    
    
    dfs_result = dfs(d,[V])
    bfs_result = bfs(V,d)


def dfs(d, visit):
    cur_node = visit[-1]
    buffer = []
    visit_set = set(visit)
    for ele in d[cur_node]:
        if ele not in visit_set:
            buffer.append(ele)

    if len(buffer) == 0:
        for ele in visit:
            print(ele, end=' ')
        print()
        return True
    
    for nxt in buffer:
        foo = dfs(d, visit + [ele])
        if foo:
            break
    
    return False

def bfs(V,d):
    pass

if __name__ == "__main__":
    solution()