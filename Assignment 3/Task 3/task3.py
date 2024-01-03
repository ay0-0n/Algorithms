inp = open("input3.txt", "r")
out = open("output3.txt", "w")

def QuickSort(arr, l, r):
    if l < r:
        q = partition(arr, l, r)
        QuickSort(arr, l, q-1)
        QuickSort(arr, q+1, r)
def partition(arr,l,r):
    pivot = arr[r]
    i = l-1
    for j in range(l, r):
        if arr[j] <= pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[r] = arr[r], arr[i+1]
    return i+1

data = inp.readlines()
for i in range(1, len(data), 2):
    arr = list(map(int, data[i].split()))
    QuickSort(arr,0,len(arr)-1)
    for j in range(len(arr)):
        out.write(str(arr[j]))
        if j!=len(arr)-1:
            out.write(' ')
    if i != len(data) - 1:
        out.write("\n")

inp.close()
out.close()


