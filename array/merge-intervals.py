class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort intervals 
        intervals.sort(key=lambda x: x[0])
        #create a retuyrn array to populate new iterval sers
        #include the first item 
        result = [intervals[0]]

        #loop through the intervals and merge the inverals that overlap

        for interval in intervals:
            left_prev_interval, right_prev_interval = result[-1][0], result[-1][1]
            left_curr_interval, right_curr_interval = interval[0],interval[1]
            #make csure to be inclusive of number
            if right_prev_interval >= left_curr_interval:
                #handle previous right interval larger than next right interval

                result[-1][1] = max(right_prev_interval, right_curr_interval)
            else:
                result.append(interval)
        
        #return the result
        return result
