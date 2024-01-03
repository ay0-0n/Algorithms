inp = open("Input Files/Task 01/part a/input1a_2.txt",'r')
out = open("output1a_2.txt", 'w')

ver, edge = tuple(map(int, inp.readline().split()))
adj_matrix = [[0]*(ver+1) for i in range(ver+1)]

while edge:
    u, v, e = tuple(map(int, inp.readline().split()))
    adj_matrix[u][v] = e
    edge -= 1

for i in range(ver+1):
    temp_n = "" if i == ver else "\n"
    for j in range(ver+1):
        temp = '' if j == ver else " "
        out.write(f"{adj_matrix[i][j]}{temp}")
    out.write(f"{temp_n}")
