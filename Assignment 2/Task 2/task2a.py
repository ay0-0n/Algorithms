inp = open("input2a.txt", "r")
out = open("output2a.txt", "w")

def MergeSort(arr, l, h):
    if l < h:
        mid = (l+h)//2
        MergeSort(arr, l, mid)
        MergeSort(arr, mid+1, h)
        Merge(arr, l, mid, h)

def Merge(arr, l, mid, h):
    n1 = mid - l+1
    n2 = h - mid
    a1 = [0] * n1
    a2 = [0] * n2
    for i in range(n1):
        a1[i] = arr[l+i]
    for j in range(n2):
        a2[j] = arr[mid+1+j]

    i,j,k = 0,0,l
    while i<n1 and j<n2:
        if a1[i] <= a2[j]:
            arr[k] = a1[i]
            i+= 1
        else:
            arr[k] = a2[j]
            j+= 1
        k+= 1

    while i<n1:
        arr[k] = a1[i]
        i, k = i+1, k+1
    while j<n2:
        arr[k] = a2[j]
        j, k = j+1, k+1

data = inp.readlines()
for i in range(1,len(data),4):
    list1 = list(map(int,data[i].split()))
    list2 = list(map(int,data[i+2].split()))
    final_list = list1 + list2
    MergeSort(final_list, 0, len(final_list)-1)
    out.write(str(final_list))
    if i != len(data) -3:
        out.write("\n")

inp.close()
out.close()