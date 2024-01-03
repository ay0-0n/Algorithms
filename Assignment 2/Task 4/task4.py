inp = open("input4.txt", "r")
out = open("output4.txt", "w")

def find_max(arr,l,h):
    if l == h:
        return arr[l]
    else:
        mid = (l+h)//2
        left_max = find_max(arr,l,mid)
        right_max = find_max(arr,mid+1,h)

        return max(left_max,right_max)

data = inp.readlines()
for i in range(1, len(data), 2):
    arr = list(map(int, data[i].split()))
    out.write(str(find_max(arr,0,len(arr)-1)))
    if i != len(data) - 1:
        out.write("\n")

inp.close()
out.close()

# The complexity of the code is O(n)