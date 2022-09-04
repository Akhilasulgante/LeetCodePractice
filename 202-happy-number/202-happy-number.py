class Solution(object):
    
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        
        def split_number(n):
            sum_ = 0
            while n>0:
                temp = n%10
                sum_ = temp*temp+sum_
                n = n/10
              
            return sum_
        visited = set()   
        while n != 1 and n != 4:
            n = split_number(n)
            
        return n == 1
            
            

            
                