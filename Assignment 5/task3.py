from queue import LifoQueue
inp = open('input3_2.txt', 'r')
out = open('output3_2.txt', 'w')

ver, edge = tuple(map(int, inp.readline().split()))
adj_list = [[] for i in range(ver + 1)]
transpose = [[] for i in range(ver + 1)]

while edge:
    u, v = tuple(map(int, inp.readline().split()))
    adj_list[u].append(v)
    transpose[v].append(u)
    edge -= 1

def DFS_visit(G, s, Stack, visited):
    visited[s] = True
    for i in G[s]:
        if not visited[i]:
            DFS_visit(G, i, Stack, visited)
    Stack.put(s)


def kosaraju(graph, tran_graph):
    visited = [False] * len(graph)
    stack = LifoQueue()
    for i in range(1, len(graph)):
        if not visited[i]:
            DFS_visit(graph, i, stack, visited)

    visited = [False]*len(graph)
    scc = []
    while stack.qsize() != 0:
        v = stack.get()
        if not visited[v]:
            temp = LifoQueue()
            DFS_visit(tran_graph, v, temp, visited)
            scc.append(sorted(list(temp.queue)))
    return scc

res = sorted(kosaraju(adj_list, transpose),key=lambda x:x[0])

for components in range(len(res)):
    next = '' if components == len(res) - 1 else '\n'
    for vals in range(len(res[components])):
        temp = '' if vals == len(res[components])-1 else ' '
        out.write(f'{res[components][vals]}{temp}')
    out.write(f'{next}')