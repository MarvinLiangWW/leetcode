class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        #solutions 1
        if n<=0: 
            return False
        return n&(n-1)==0
        
        # solutions 2
        if n == 0:
            return False
        while n%2 == 0: 
            n/=2
        return n == 1
        
        # solution 3
        # count 1s
        return n > 0 and sum([int(i) for i in bin(n)[2:]]) == 1
