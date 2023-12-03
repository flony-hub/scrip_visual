class Solution:
    def reverse(self, x:int ) -> int:
        if x<0:
            x *=-1
            inverso = 0
            while(x !=0):
                inverso= inverso *10 + x %10
                x = int (x/10)
            return inverso *-1
        else:
            inverso = 0
            while(x !=0):
                inverso= inverso *10 + x %10
                x = int (x/10)
            return inverso 
        
a = 1534236469
ver = Solution()
print (ver.reverse(a))