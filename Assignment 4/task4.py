inp = open("Input Files/Task 04/input4_5.txt", 'r')
out = open("output4_5.txt", 'w')

ver, edge = tuple(map(int, inp.readline().split()))
adj_list = [[] for i in range(ver + 1)]

while edge:
    u, v = tuple(map(int, inp.readline().split()))
    adj_list[u].append(v)
    edge -= 1


def has_cycle_dfs(G):
    color = ['white'] * (len(G))

    def dfs_visit(G, s):
        color[s] = 'grey'
        for i in G[s]:
            if color[i] == 'grey':
                return True
            elif color[i] == 'white':
                if dfs_visit(G, i):
                    return True
        color[s] = 'black'
        return False

    for i in range(1, len(G)):
        if color[i] == 'white':
            if dfs_visit(G, i):
                return "YES"
    return "NO"
out.write(f"{has_cycle_dfs(adj_list)}")
