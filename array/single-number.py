class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new_set = set()
        for num in nums:
            if num not in new_set:
                new_set.add(num)
            else:
                new_set.remove(num)

            
        return_num = new_set.pop()
        return return_num

            
