# def printNumbers():
#     for i in range(1, 11):
#         print (i)
# printNumbers()
#recursive function

# def sum(n):
#     if n==1:
#         return 1
#     return n + sum(n-1)
# print(sum(5))


def twoSum(arr, target):
    for i in range(0, len(arr)-1):
        firstNum = arr[i]
        for j in range(i+1, len(arr)):
            secondNum = arr[j]
            if firstNum + secondNum== target:
                return True
    return False

print(twoSum([3,5,5,4,6], 12))
