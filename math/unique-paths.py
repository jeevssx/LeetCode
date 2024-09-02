class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #since we dont have access to a grid or or rows/colums we DP bottom up
        #m = row , n = columns
        #init a starter temp row
        prevRow = [0] * n

        #for cell in range of bottom rows to 0 decrementing by 1 each time
        for r in range(m - 1, -1, -1):
            #init the current row to have n 0s for each col
            currRow = [0] * n
            #set the finish to 1 so we can work bottom up(would technically be 0)
            #the 1 represents the paths from the curr spot to the finish spot
            currRow[n - 1] = 1
            #^ the paths from the right most column to end is also one so we are allowed this

            #start another loop to start the summation
            #for all columns in the row to the left of the end column
            for c in range(n - 2, -1 , -1):

                #add the right cell with bottom cell since those are only allowed directions
                #for each cell in row
                currRow[c] = currRow[c + 1] + prevRow[c]
            #after each cell in row, reassign the prevRow with the curr Row and restart process 
            prevRow = currRow
        
        return prevRow[0]
        #which is the start
