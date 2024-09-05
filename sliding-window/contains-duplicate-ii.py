class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #create a set to store the values -> fixed sliding window problem 

        window = set()
        L = 0

        for R in range(len(nums)):
            # R-L: will remove the value thats out of the window when we slide it over
            #goofy case where abs(i-j) <= k so its off by 1
            if R - L > k:
                window.remove(nums[L])
                L+=1


            #add the check if the num is in the window
            if nums[R] in window:
                return True
            #add to hashset just like contain dup1
            window.add(nums[R])

        return False