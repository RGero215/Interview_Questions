import tokenize
import inspect

nums = [1,2,3]
# define a function name recursion that takes a list of numbers name nums and index default 0
def recursion(nums, index=0):
    '''
    This function traverse a list recursibly
    '''
    # create a current variable starting at the first index of nums
    current = nums[0]
    # create a last_item varible with nums last item
    last_item = nums[len(nums) - 1]
    # check if index is equal to last_item
    if index == last_item:
        print('Current: ', current)
        # return current
        return current
    # assign the nums index to current
    current = nums[index]
    print('Current: ', current)
    # return recursion incrementing index by one
    return recursion(nums, index+1)

print(recursion([1,2,3,4,5]))

fileObj = open('recursion.py', 'r')
for toktype, tok, start, end, line in tokenize.generate_tokens(fileObj.readline):
    # we can also use token.tok_name[toktype] instead of 'COMMENT'
    # from the token module 
    if toktype == tokenize.COMMENT:
        print('COMMENT' + " " + tok)
        print('CODE: {}'.format(raw_input()))
    
        

# print(inspect.getsource(recursion))

