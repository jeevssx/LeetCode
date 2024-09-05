class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #create hash map - map charCount to List of Anagrams

        for s in strs:
            count = [0] * 26 #a....z

            for c in s:
                count[ord(c) - ord("a")] += 1
            
            res[tuple(count)].append(s)
        
        return res.values()

        #o(m * n)
        