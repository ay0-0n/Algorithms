inp = open('input1_3.txt', 'r')
out = open('output1_3.txt', 'w')

n = int(inp.readline())
data = []

for i in range(n):
    s, f = list(map(int, inp.readline().split()))
    data.append((s, f))

time = sorted(data, key=lambda x: x[1])
ans = [time[0]]
pointer = 0

for i in range(1,n):
    u, v = time[i]
    if u >= ans[pointer][1]:
        ans.append(time[i])
        pointer += 1

out.write(f'{len(ans)}\n')
for i in range(len(ans)):
    temp = '\n' if i != len(ans)-1 else ''
    out.write(f'{ans[i][0]} {ans[i][1]}{temp}')