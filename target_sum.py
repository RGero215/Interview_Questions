def twoNumberSum(array, targetSum):
    for i in range(len(array) - 1):
        firstNum = array[i]
        print('FirstNum: ', firstNum)
        for j in range(i + 1, len(array)):
            secondNum = array[j]
            print('Second: ', secondNum)
            print('Value: ', firstNum + secondNum)
            if firstNum + secondNum == targetSum:
                print('Result: ', [firstNum, secondNum])
                return [firstNum, secondNum]
    return []

# def twoNumberSum(array, targetSum):
#     nums = {}
#     for num in array:
#         if targetSum - num in nums:
#             return [targetSum - num, num]
#         else:
#             nums[num] = True
#     return []

# def twoNumberSum(array, targetSum):
#     array.sort()
#     left = 0
#     right = len(array) - 1
#     while left < right:
#         currentSum = array[left] + array[right]
#         if currentSum == targetSum:
#             print([array[left], array[right]])
#             return [array[left], array[right]]
#         elif currentSum < targetSum:
#             left += 1
#         elif currentSum > targetSum:
#             right -= 1
#     print([])
#     return []


twoNumberSum([3,5,-4,8,11,1,-1,6], 10)

if __name__ == "__main__":
    pass


