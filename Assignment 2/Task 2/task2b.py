inp = open("input2b.txt", "r")
out = open("output2b.txt", "w")

def Merge(a1,a2):
    new_arr = [0]*(len(a1)+len(a2))
    i, j, k = 0, 0, 0
    while i<len(a1) and j<len(a2):
        if a1[i] <= a2[j]:
            new_arr[k] = a1[i]
            i += 1
        else:
            new_arr[k] = a2[j]
            j +=1
        k+= 1
    while i<len(a1):
        new_arr[k] = a1[i]
        i, k = i+1, k+1
    while j<len(a2):
        new_arr[k] = a2[j]
        j, k = j+1, k+1
    return new_arr




data = inp.readlines()
for i in range(1,len(data),4):
    list1 = list(map(int,data[i].split()))
    list2 = list(map(int,data[i+2].split()))
    out.write(str(Merge(list1,list2)))
    if i != len(data) -3:
        out.write("\n")