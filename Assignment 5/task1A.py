inp = open('input1A_2.txt', 'r')
out = open('output1A_2.txt', 'w')

ver, edge = tuple(map(int, inp.readline().split()))
adj_list = [[] for i in range(ver + 1)]

while edge:
    u, v = tuple(map(int, inp.readline().split()))
    adj_list[u].append(v)
    edge -= 1

def DFS(G):
    global visited, time, start_time, finish_time, cycle
    visited = [False]*len(G)
    time = 0
    start_time = [0]*len(G)
    finish_time = [0]*len(G)
    cycle = False
    for i in range(1, len(G)):
        if not visited[i]:
            DFS_visit(G, i)

    return cycle, finish_time[1:]

def DFS_visit(G, s):
    global visited, time, start_time, finish_time, cycle
    visited[s] = True
    time = time + 1
    start_time[s] = time
    for i in G[s]:
        if not visited[i]:
            DFS_visit(G, i)
        else:
            if start_time[s] > start_time[i] and finish_time[i] == 0:
                cycle = True
    time = time + 1
    finish_time[s] = time

cycle, finish  = DFS(adj_list)
if cycle:
    out.write("Impossible")
else:
    dict = {i+1: finish[i] for i in range(len(finish))}
    res = sorted(dict.items(), key = lambda x: x[1], reverse=True)
    for i in range(len(res)):
        out.write(f"{res[i][0]} ")