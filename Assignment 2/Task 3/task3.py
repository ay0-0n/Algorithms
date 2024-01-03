inp = open("input3.txt", "r")
out = open("output3.txt", "w")

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        a1 = mergeSort(arr[:mid])
        a2 = mergeSort(arr[mid:])
        return merge(a1, a2)

def merge(a,b):
    arr =[0]*(len(a)+len(b))
    i = j = k = 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1

    while i < len(a):
        arr[k] = a[i]
        i, k = i+1, k+1
    while j < len(b):
        arr[k] = b[j]
        j, k = j+1, k+1

    return arr

data = inp.readlines()
for i in range(1, len(data), 2):
    arr = list(map(int, data[i].split()))
    out.write(str(mergeSort(arr)))
    if i != len(data) - 1:
        out.write("\n")

inp.close()
out.close()


