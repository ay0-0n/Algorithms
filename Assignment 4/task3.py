inp = open("Input Files/Task 03/input3_4.txt", 'r')
out = open("output3_4.txt", 'w')

ver, edge = tuple(map(int, inp.readline().split()))
adj_list = [[] for i in range(ver + 1)]

while edge:
    u, v = tuple(map(int, inp.readline().split()))
    adj_list[u].append(v)
    adj_list[v].append(u)
    edge -= 1


def Dfs(G, s):
    color = ['white']*(len(G))
    res = []
    def Dfs_visit(G, s):
        color[s] = 'grey'
        res.append(s)
        for i in G[s]:
            if color[i] == 'white':
                Dfs_visit(G, i)
        color[s] = 'black'
    Dfs_visit(G, s)
    res_str = ' '.join(str(i) for i in res)
    return res_str

out.write(Dfs(adj_list, 1))
