class Solution:
    def isHappy(self, n: int) -> bool:
        if n==1:
            return True
        elif n==4:
            return False
        sum=0
        while n>0:
            base=n%10
            sum=sum+(base*base)
            n=n//10
        return self.isHappy(sum)
