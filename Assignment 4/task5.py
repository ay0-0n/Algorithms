from queue import Queue

inp = open("Input Files/Task 05/input5_4.txt", 'r')
out = open("output5_4.txt", 'w')

ver, edge, dest = tuple(map(int, inp.readline().split()))
adj_list = [[] for i in range(ver + 1)]

while edge:
    u, v = tuple(map(int, inp.readline().split()))
    adj_list[u].append(v)
    adj_list[v].append(u)
    edge -= 1


def Bfs(G, s):
    Q = Queue()
    Q.put(s)
    color = ['white']*len(G)
    parents = [None]*len(G)
    distance = [float('-inf')]*len(G)
    color[s] = 'grey'
    distance[s] = 0
    while Q.qsize() != 0:
        u = Q.get()
        for i in G[u]:
            if color[i] == 'white':
                color[i] = 'grey'
                distance[i] = distance[u] + 1
                parents[i] = u
                Q.put(i)
        color[u] = 'black'
    return parents, distance

def shortest_path(G, destination):
    source = 1
    parents, distance = Bfs(G, source)
    path = []
    curr = destination
    while curr is not None:
        path.append(curr)
        curr = parents[curr]

    return path,distance[destination]


path, time = shortest_path(adj_list, dest)
out.write(f"Time: {time}\nShortest Path: ")

for i in range(len(path)-1, -1, -1):
    temp = '' if i == 0 else ' '
    out.write(f"{path[i]}{temp}")