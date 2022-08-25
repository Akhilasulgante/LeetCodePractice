class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #build a hash table with freq count
        # Time complexity = O(N * M)
        
        res = defaultdict(list)
        # res ={}
        for s in strs:
            count = [0]*26
            
            for c in s:
                count[ord(c) - ord('a')] += 1
                
            res[tuple(count)].append(s)
            
        
        return res.values()
        