inp = open("input2.txt","r")
out = open("output2.txt", "w")

def Bubble_Sort(arr,n):
    for i in range(n-1):
        flag = False
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                flag = True
        if (flag==False):
            break
len_arr1 = int(inp.readline())
arr1 = [int(i) for i in inp.readline().split()]
Bubble_Sort(arr1, len_arr1)
out.write(str(arr1))

out.write("\n")

len_arr2 = int(inp.readline())
arr2 = [int(i) for i in inp.readline().split()]
Bubble_Sort(arr2, len_arr2)
out.write(str(arr2))

inp.close()
out.close()