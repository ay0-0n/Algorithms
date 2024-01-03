inp = open("input1.txt", "r")
out = open("output1.txt", "w")


def _mergeSort(arr,l,r):
    inv = 0
    if l < r:
        mid = (l+r)//2
        inv += _mergeSort(arr, l, mid)
        inv += _mergeSort(arr, mid+1, r)
        inv += merge(arr, l, mid, r)

    return (inv)
def merge(arr, l, mid, r):
    inv = 0
    n1 = mid - l + 1
    n2 = r - mid
    a1 = [0]*n1
    a2 = [0]*n2
    for i in range(n1):
        a1[i] = arr[l+i]
    for j in range(n2):
        a2[j] = arr[mid+1+j]
    i = j = 0
    k = l
    while i <n1 and j <n2:
        if a1[i] < a2[j]:
            arr[k] = a1[i]
            i += 1
        else:
            arr[k] = a2[j]
            j += 1
            inv += n1 - i
        k += 1

    while i < n1:
        arr[k] = a1[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = a2[j]
        j += 1
        k += 1
    return inv


data = inp.readlines()
for i in range(1, len(data), 2):
    arr = list(map(int, data[i].split()))
    out.write(str(_mergeSort(arr,0,len(arr)-1)))
    if i != len(data) - 2:
        out.write("\n")

inp.close()
out.close()
