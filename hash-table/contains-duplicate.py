class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #create a set
        newSet = set()
        #for loop and iterate through
        for num in nums:
        #add each number to the set
            if num in newSet:
                return True
            newSet.add(num)
       
        return False
   
          

        #exit the loop return false