"""
    Searching And Sorting : 

    Searching : 
    -Linear Search
        -> Works on Sorted and unsorted list
        -> Simple to Understand
        -> Slow for large list

    -Binary Search : 
        Binary Search Divides the list into two halves and searches efficiently

        -> List Must be sorted
        -> Faster than Linear Search
        -> Uses divide and conquer Technique
"""
# Linear Search
# li=[1,2,3,4,5,6,7,8,9,10]
# n=int(input("Enter Number to Search : "))
# for i in li:
#     if i==n:
#         print("Number Found")
#         break
# else:
#         print("Number Not Found")

# li=[1,2,3,4,5,6,7,8,9,10]
# n=int(input("Enter Number To Search : "))
# low=0
# high=len(li)-1
# while low<=high:
#      mid=(low+high)//2
#      if li[mid]==n:
#           print("Number Found")
#           break
#      elif n>mid:
#           low=mid+1
#      else:
#           high=mid-1
# else:
#      print("Number Not Found")

# Sorting : 
"""
Refers to organize the provide list in ascending or descending format.
-Bubble Sort
-Selection Sort
-Insertion Sort
"""

# Bubble Sort : 
"""
Bubble Sort repeatedly swaps adjacent elements if they are wrong in order.

-> Largest Element moves to end
-> Very Easy to understand
-> Slow for large data

"""
# li=[6,5,7,4,3,2,1,8,9,10]
# for i in range(len(li)):
#      for j in range(i+1,len(li)-1):
#           if li[i]>li[j]:
#                li[i],li[j]=li[j], li[i]
# print(li)


"""
Selection Sort : 
Selects the smallest element and places it at correct position.
"""
arr=[1,2,3,6,5,4,7,8,9,10]
for i in range(len(arr)):
    min=i
    for j in range(i+1,len(arr)):
          if arr[j]<arr[min]:
               min=j
    arr[i],arr[min]=arr[min],arr[i]

# Time Complexity : 
"""
Linear Search : 
O(n)
Binary Search : 
O(log n)

Bubble Sort : 
O(n^2)

Selection Sort : 
O(n^2)
"""