class Solution:
    def climbStairs(self, n: int) -> int:
        #we can do bottom up true dp - problem is kind of like reverse fibonacci
        #the idea is that the amount of ways to get to the last stair from n-1 
        #will always be 1 while for n-2 it will always be 2 and n-3 will be 3
        #for 4 it will be 5
        # the base forumla is that for the ith stair it would be (i+1) + (i+2) = i
        #so if we want the total paths we would just compute from n to the start

        #one = (n-1) val technically n should have 0 ways to get to n but to make math work out we should have it set to one
        #two = n 

        #base cases
        one, two = 1, 1

        #pretty much walking backwards
        #range(n=5) would be for i from 0->4
        #so range(n-1) will make us start from n-2
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        
        return one