class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        
        for i in range(len(strs[0])):
            for s in strs:
                if (len(s) == i) or (s[i] != strs[0][i]):
                    return res
            res += strs[0][i]
            
        return res
            