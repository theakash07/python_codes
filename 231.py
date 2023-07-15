class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        ans=1
        m=n
        cout=0
        if n<0:
             return False
        while n!=0:
             digit=n%2
             if digit==0 :
                 cout=cout+1
             n=n//2
    
    
        if 2**cout==m:
             return True
        else:
             return False
    
        
