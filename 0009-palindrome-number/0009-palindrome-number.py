class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp=x
        rev=0
        if x<0:
            x=x*-1

        while x>0:
            rem=x%10
            rev=rev*10+rem
            x=x//10
        return temp==rev

        