class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        newSet = set(nums) #turn nums into a set

        longest = 0 #keet a variable that can keep track of the longestConsecutive

        for num in nums: #for loop to check through nums using num to access each num

            if (num - 1) not in newSet: #check if its the start of sequence because no left node

                length = 1 #keep track of the current length of the sequence

                while (num + length) in newSet: #while num + length is in numSet we can increment length

                    length += 1 # increment the length varible so while keeps running until last num in seq
            
                longest = max(length, longest) #set longest as which is longer: current len or longest len

        return longest #duh

