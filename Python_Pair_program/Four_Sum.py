# input: [7, 6, 4, -1, 1, 2], 16 # {13: [7, 6], 10: [[6,4]], 3: [[4,-1]]}
        #   i   j         i  j
# output: [[7, 6, 4, -1], [7, 6, 1, 2]]

def fourNumberSum(array, targetSum):
    # hash
    seen = {} # {13: [[7, 6]], 10:[[6, 4]], 3:[[4, -1], [1, 2]]}
                                                #   0       1
    # array for quadruples
    results_list = []
    result = [] # [4, -1, 7, 6]
    # fill in hashtable
    i = 0 # 2 # less than index 4
    j = 1 # 3 # less than index 5
    while i <=len(array) - 2 and j <= len(array) - 1:
        val_sum = array[i] + array[j]  
        val_list = [[array[i], array[j]] ]
        seen[val_sum] = val_list # 3:[[4, -1]]
        diff = targetSum - val_sum # 16 - 3 = 13

        # handle duplication
        if diff == val_sum:
            continue
        if diff in seen: 
            complement_vals = seen[diff] # [[7, 6]]
            result.append(val_list[0][0])
            result.append(val_list[0][1])
            result.append(complement_vals[0][0]) 
            result.append(complement_vals[0][1]) 
            results_list.append(result)
            result = []
            # for item in result:
            
    
        i += 1
        j += 1 
        # result 
    return results_list

#     File "Four_Sum.py", line 17
#     seen[val_sum] = val_list # 3:[[4, -1]]
#        ^
# SyntaxError: invalid syntax

if __name__ == "__main__":
    arr = [7, 6, 4, -1, 1, 2]
    
    targetSum = 16
    print(fourNumberSum(arr, targetSum))      

        
    # loop to find complement pair
    # from range 1 to len -1 i
        # range i + 1 to len j
            #currSum = arr[i] + arr[j]
            # diff = target - current
            # check if diff in hash
                # seen[diff] += val_list = {3: [[4,-1]]}

# Solution Ideas
# - four for loops
# - sliding window

# f = [7, 6] => 13
# s = [4, -1] => 3
# x = 13 
# y = 3
#hash = 
# {
#     13: [[7, 6]],
#     3: [[4, -1],[1, 2]]
#     10: [[6,4]]
#     0: [[-1, 1]]

# }