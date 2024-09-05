class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0 #set a counter so that for an elemnt if it increments it will be the most

        candidate = 0 #candiate number that is being checked in the iteration of the loop

        for num in nums: #for loop that iterates through the array nums and num to access inidvidual

            if count == 0: #if the count of the variable is 0

                candidate = num #then we can set the candiaite we are checking to the num of the loop

            if num == candidate: #however if we find another of the element we increment the count by 1

                count += 1 #increment count by 1

            else: #if we dont increment it by 1 then we 

                count -= 1 #decrement it by 1: so if it ever turns 0 it goes to the next element and d
                #increments an decrements agian for the process
 
        return candidate #return the candidate that is last left standing
