inp = open("input3.txt","r")
out = open("output3.txt", "w")

n = int(inp.readline())
id = list(map(int,inp.readline().split()))
num = list(map(int,inp.readline().split()))

for i in range(n-1):
    max = i
    for j in range(i+1,n):
        if num[j] > num[max]:
            max = j
        elif num[j] == num[max] and id[j]<id[max]:
            max = j
    num[i],num[max] = num[max],num[i]
    id[i], id[max] = id[max], id[i]

for i in range(n):
    nl = "\n" if i!=n-1 else ""
    out.write(f"ID: {id[i]} Mark: {num[i]}{nl}")

inp.close()
out.close()