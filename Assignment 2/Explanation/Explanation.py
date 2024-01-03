print("# Task 1")
print("###############################################")
print("""1. We run the outer for loop to select every element one by one, then compare it by using the inner
for loop to see if we can find another element in the rest of the array that can add up to target.If we 
find it, we just store it in a variable incrementing +1 (1 base indexing) and we break the loop. As were
using two loops the complexity is 0(n^2)""")
print()
print("""2. Here, While iterating through every element, Every time we check how much closer we are to the 
target. Then we just perform a binary search on the rest of the array top see if the remaining is in our
array. Here as i'm using a for loop ranged n and binary seaech which is O(log2n). The overall complexity
of my code is O(nlog2n)""")
print()
print("# Task 2")
print("###############################################")
print("""1. We can combine the two list and simply use merge sort. We know Merge Sort has the time complexity
of O(nlogn). Merge sort is a divide and conquer algorithm where we first recursively divide the array
into single elements and conquer them by 2-way merge using the Merge function""")
print()
print("""2. To achieve a time complexity of o(n), instead of merging the 2 arrays like I did in question 1,
I can just use 2-way merge as both of the arrays are sorted. Here, we take 3 pointers and an external array.
We can just check for the minimum element between the two arrays and keep inserting them in our external array
using our third pointer. When one of the pointer of two arrays reaches the end we can just end the loop
and insert the remaining elements of the other array in the external array. In this way we can get a linear 
time complexity of O(n)""")
print()
print("# Task 3")
print("###############################################")
print("""We're asked to sort the arrays using merge sort. Merge sort is a divide and conquer algorithm.In the 
mergeSort function we device the array into subarrays, recursively sorts each subarray, and in the merge 
function we merge them to produce a sorted array.In the merge funcyion we compare elements from the two subarrays
and place them in the correct order, resulting in a sorted array at the end. It has a comlexity of O(nlogn)""")
print()
print("# Task 4")
print("###############################################")
print("""Here we find the maximum values using divide and conquer approch. The base case when l = h, it means there's 
only one element, so we just return that element. We divide the array into equal left and right portion each time 
returning maximum of the two subarrays.""")