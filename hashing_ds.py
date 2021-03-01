def isSubset(arr1, arr2, m, n):
    mp = {}
    for i in range(n):
        mp[arr2[i]] = 0
    for i in range(m):
        mp[arr1[i]] = 1

    for i in range(n):
        if mp[arr2[i]] != 1:
            return "No"
    return "Yes"

arr1 = [11, 1, 13, 21, 3, 7]
arr2 = [11, 3, 21, 1,10]

m = len(arr1)
n = len(arr2)
print(isSubset(arr1, arr2, m, n))

def countmaxSubset(arr1,arr2,m,n):
    mp = {}
    count = n
    for i in range(n):
        mp[arr2[i]] = 0
    for i in range(m):
        mp[arr1[i]] = 1

    for i in range(n):
        if mp[arr2[i]] != 1:
            count = count -1
    return count
arr1 = [11, 1, 13, 21, 3, 7]
arr2 = [11, 3, 21, 1,10]
m = len(arr1)
n = len(arr2)
print(countmaxSubset(arr1,arr2,m,n))



def printmaxSubset(arr1,arr2,m,n):
    mp = {}
    arr = arr2.copy()
    for i in range(n):
        mp[arr2[i]] = 0
    for i in range(m):
        mp[arr1[i]] = 1

    for i in range(n):
        if mp[arr2[i]] != 1:
            arr.remove(arr2[i])

    return arr
arr1 = [11, 1, 13, 21, 3, 7]
arr2 = [11, 3, 21, 1,10]
m = len(arr1)
n = len(arr2)
print(printmaxSubset(arr1,arr2,m,n))

# Sorting using hashing

def HashingSort(arr):
    mp = {}
    Max = 0
    for i in range(1,100):
        mp[i] = 0

    for i in range(len(arr)):
        mp[arr[i]] = 1
        Max = max(Max,arr[i])

    for i in range(1,Max+1):
        if mp[i] != 0:
            print(i, end=" ")
a = [9, 4, 3, 2, 5, 2, 1, 0, 4,
         3, 5, 10, 15, 12, 18, 20, 19]
# HashingSort(a)

def firstElement(arr,k):
    mp = {}
    for i in range(len(arr)):
        mp[arr[i]] = 0

    for i in range(len(arr)):
        mp[arr[i]] += 1

    for key,v in mp.items():
        if v == k:
            print(key,end=" ")

arr = [1, 7, 4, 3, 4, 8, 7]
k = 2
firstElement(arr, k)
