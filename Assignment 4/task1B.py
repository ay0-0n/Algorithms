inp = open("Input Files/Task 01/part b/input1b_3.txt",'r')
out = open("output1b_3.txt", 'w')

ver, edge = tuple(map(int, inp.readline().split()))
adj_list = [[] for i in range(ver+1)]

while edge:
    u, v, e = tuple(map(int, inp.readline().split()))
    adj_list[u].append((v, e))
    edge -= 1

for i in range(ver+1):
    temp_n = "" if i == ver else "\n"
    out.write(f"{i} : ")
    for j in range(len(adj_list[i])):
        temp = '' if j == ver else " "
        out.write(f"{adj_list[i][j]}{temp}")
    out.write(f"{temp_n}")