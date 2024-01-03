import heapq
inp = open('input2_3.txt', 'r')
out = open('output2_3.txt', 'w')

ver, edge = tuple(map(int, inp.readline().split()))
adj_list = [[] for i in range(ver + 1)]

in_degree = [0]*(ver+1)

while edge:
    u, v = tuple(map(int, inp.readline().split()))
    adj_list[u].append(v)
    in_degree[v] += 1
    edge -= 1

def Bfs(G, indeg):
    Q = []
    for i in range(1, len(G)):
        if indeg[i] == 0:
            heapq.heappush(Q, i)
    order = []
    while len(Q) != 0:
        u = heapq.heappop(Q)
        order.append(u)
        for i in G[u]:
            indeg[i] -= 1
            if indeg[i] == 0:
                heapq.heappush(Q, i)
    return order if len(order) == len(G)-1 else None

course_order = Bfs(adj_list, in_degree)
if course_order is None:
    out.write("IMPOSSIBLE")
else:
    course = str(course_order)[1:-1].split(',')
    for i in range(len(course)):
        out.write(course[i])