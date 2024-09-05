class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        #each index needs to be the sum of the previous indicie
        '''
        nums = [1,2,3,4]
                    
        output: [1,3,6,10]

        for i, num in enumerate(nums): gives index and num for each
        
            changingValue = 0
            while (i > 0): while loop to go back through each prev and add sum
            
                changedValue += num[i]

                i -= 1 so that it can dec
            assign the value after as the new one at that i
            nums[i] = changedValue

                

        '''
        for i in range(1, len(nums)):
                nums[i] += nums[i-1] 
        return nums
            
    
        



            
             