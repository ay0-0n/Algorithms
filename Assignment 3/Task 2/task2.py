inp = open("input2.txt", "r")
out = open("output2.txt", "w")

def find(arr):
    temp = 0
    for i in arr:
        if abs(i)>temp:
            temp = abs(i)
    return temp**2


def get_max(a):
     n = len(a)
     mid = n//2
     if n==1:
         return -9999999
     if n==2:
         return a[0] + a[1]**2
     left = get_max(a[:mid])
     right = get_max(a[mid:])

     cross_max = max(a[:mid]) + find(a[mid:])

     return max(left,right,cross_max)

data = inp.readlines()
for i in range(1, len(data), 2):
    arr = list(map(int,data[i].split()))
    out.write(str(get_max(arr)))
    if i != len(data) -1:
        out.write("\n")

inp.close()
out.close()