inp = open("input1.txt", "r")
out = open("output1.txt", "w")


# 1 (O(n**2))
def n_square_sum(arr, n, target):
    a, b = None, None
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                a, b = i + 1, j + 1
                break
        break

    res = f'{a} {b}' if a is not None and b is not None else 'IMPOSSIBLE'
    out.write(res)


data = inp.readlines()
for i in range(0, len(data), 2):
    n, target = tuple(map(int, data[i].split()))
    arr = list(map(int, data[i + 1].split()))
    n_square_sum(arr, n, target)
    if i != len(data) - 2:
        out.write("\n")

# 2 (O(logn))
def binary_search(arr, low, high, target):
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return None

def logn_solution(arr, n, target):
    a, b = None, None
    for i in range(n):
        to_find = target - arr[i]
        temp = binary_search(arr,i,n-1,to_find)
        if temp is not None:
            a, b = i+1, temp +1
            break
    res = f'{a} {b}' if a is not None and b is not None else 'IMPOSSIBLE'
    out.write(res)

out.write('\n')
for i in range(0, len(data), 2):
    n, target = tuple(map(int, data[i].split()))
    arr = list(map(int, data[i + 1].split()))
    logn_solution(arr, n, target)
    if i != len(data) - 2:
        out.write("\n")

inp.close()
out.close()
