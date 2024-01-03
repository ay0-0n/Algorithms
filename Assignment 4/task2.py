from queue import Queue

inp = open("Input Files/Task 02/input2_4.txt", 'r')
out = open("output2_4.txt", 'w')

ver, edge = tuple(map(int, inp.readline().split()))
adj_list = [[] for i in range(ver + 1)]

while edge:
    u, v = tuple(map(int, inp.readline().split()))
    adj_list[u].append(v)
    adj_list[v].append(u)
    edge -= 1


def Bfs(G, s):
    Q = Queue()
    Q.put(s)
    visited = ['white']*len(G)
    visited[s] = 'grey'
    res = ''
    while Q.qsize() != 0:
        u = Q.get()
        res += str(u) + ' '
        for i in G[u]:
            if visited[i] == 'white':
                visited[i] = 'grey'
                Q.put(i)
        visited[u] = 'black'
    return res[:-1]


out.write(f"{Bfs(adj_list, 1)}")
