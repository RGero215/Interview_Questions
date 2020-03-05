class Solution(object):
    def productExceptSelf(self, nums):
        
        output = [1] * len(nums)
        print("Output: ", output)
        prod = 1
        print("**************************")
        for i in range(len(nums)):
            output[i] *= prod
            prod *= nums[i]
            print("Output: ", output)
            print("prod: ", prod)
        print("=============================")
        
        prod = 1
        for i in range(len(nums) -1, -1, -1):
            output[i] *= prod
            prod *= nums[i]
        print("Output: ", output)
        print("prod: ", prod)
        print("=============================")
        
        print(output)
        return output

if __name__ == "__main__":
    
    nums = [1,2,3,4]
    # output [24,12,8,6]
    solution = Solution()
    solution.productExceptSelf(nums)

    # Creating a dictionary 
    myDict = {1: 'Geeks', 2: 'For', 3: 'Geeks'} 

    # Iterating through the keys 
    for key in myDict.keys(): 
        if key == 2: 
            del myDict[key] 

    # Modified Dictionary		 
    print(myDict) 
