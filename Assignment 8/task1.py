inp = open('input1_2.txt', 'r')
out = open('output1_2.txt', 'w')

n, m = list(map(int, inp.readline().split()))
adj_matrix = [[0]*(n+1) for i in range(n + 1)]

for i in range(m):
    u, v, w = list(map(int, inp.readline().split()))
    adj_matrix[u][v] = w
    adj_matrix[v][u] = w


def find_par(u, par):
    if par[u] == u:
        return u
    return find_par(par[u], par)


def Kruskal(G):
    par = list(range(len(G)))
    edge_list = []
    cost = 0

    edges = []
    for u in range(1,len(G)):
        for v in range(1, len(G)):
            if G[u][v] != 0:
                edges.append((u, v, G[u][v]))

    edges.sort(key=lambda edge: edge[2])
    for u, v, w in edges:
        par_u = find_par(u, par)
        par_v = find_par(v, par)

        if par_u != par_v:
            par[par_u] = par_v
            edge_list.append((u, v, w))
            cost += w

    return cost

out.write(f'{Kruskal(adj_matrix)}')