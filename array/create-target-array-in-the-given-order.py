class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        # arr = []
        # for num, i in enumerate(nums):
        #     value = index[i]
        #     arr.insert(value, num)
        # return arr



        # create a new arr
        # for loop look at nums[i] and index[i], then insert there


        target_array = []
        for i,num in enumerate(nums):
            indexVal = index[i]
            target_array.insert(indexVal, num)
        return target_array
            
