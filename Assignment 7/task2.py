inp = open('input2_4.txt', 'r')
out = open('output2_4.txt', 'w')

n, m = list(map(int, inp.readline().split()))

tasks = []

for i in range(n):
    s, f = list(map(int, inp.readline().split()))
    tasks.append((s, f))

time = sorted(tasks, key=lambda x: x[1])

counter = 0
availability = [0] * m
done = {time[i]: False for i in range(len(time))}
for intervals in time:
    for i in range(m):
        if not done[intervals]:
            if intervals[0] >= availability[i]:
                availability[i] = intervals[1]
                counter += 1
                done[intervals] = True
                break

out.write(str(counter))
inp.close()
out.close()