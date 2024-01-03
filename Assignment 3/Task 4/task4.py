inp = open("input4.txt", "r")
out = open("output4.txt", "w")

def kth_smallest_num(arr,l,r,k):
    if l == r:
        return arr[l]
    else:
        idx = partition(arr, l, r)
        if idx + 1 == k:
            return arr[idx]
        elif idx+1 > k:
            return kth_smallest_num(arr,l,idx-1,k)
        else:
            return kth_smallest_num(arr,idx+1,r,k)

def partition(arr,l,r):
    pivot = arr[r]
    i = l-1
    for j in range(l, r):
        if arr[j] <= pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[r] = arr[r], arr[i+1]
    return i+1

n = int(inp.readline())
arr = list(map(int,inp.readline().split()))
queries = int(inp.readline())
for i in range(queries):
    out.write(str(kth_smallest_num(arr,0,n-1,int(inp.readline()))))
    if i != queries - 1:
        out.write("\n")

inp.close()
out.close()