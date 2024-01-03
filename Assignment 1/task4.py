inp = open("input4.txt","r")
out = open("output4.txt", "w")

n = int(inp.readline())
train = []
dt = []
time = []
for i in range(n):
    temp = inp.readline().split()
    train.append(temp[0])
    dt.append(temp[4])
    time.append(temp[-1])

def selectionSort(train, dt, time, size):
  for i in range(size-1):
    min = i
    for j in range(i+1, size):
      if train[j] < train[min]:
        min = j
      if train[j] == train[min]:
        if time[j] > time[min]:
          min = j

    train[i], train[min] = train[min], train[i]
    time[i], time[min] = time[min], time[i]
    dt[i], dt[min] = dt[min], dt[i]

selectionSort(train, dt, time, n)

for i in range(n):
  nl = "\n" if i!=n-1 else ""
  out.write(f"{train[i]} will departure for {dt[i]} at {time[i]}{nl}")