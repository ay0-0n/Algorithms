import heapq
inp = open('input3_2.txt', 'r')
out = open('output3_2.txt', 'w')

n, m = list(map(int, inp.readline().split()))

adj_list = [[] for i in range(n+1)]

for i in range(m):
    u, v, e = list(map(int, inp.readline().split()))
    adj_list[u].append((v, e))

def Dijkstra(G,s):
    distance = [99999]*len(G)
    distance[s] = 0


    priority_Q = []
    heapq.heapify(priority_Q)
    heapq.heappush(priority_Q, (0, s))

    while len(priority_Q) != 0:
        dist, curr = heapq.heappop(priority_Q)

        for i,w in G[curr]:
                temp = max(dist,w)
                if temp < distance[i]:
                    distance[i] = temp
                    heapq.heappush(priority_Q, (temp, i))

    return distance[len(G)-1]

out.write(f'{Dijkstra(adj_list, 1)}')