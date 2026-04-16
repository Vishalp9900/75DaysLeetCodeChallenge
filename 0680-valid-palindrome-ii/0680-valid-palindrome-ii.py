class Solution:
    
    def isStrPalindrome(self,s,i,j):
        while i<j:
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True
    def validPalindrome(self, s: str) -> bool:
        left,right=0,len(s)-1

        while left<right:
            if s[left]!=s[right]:
                return self.isStrPalindrome(s,left,(right-1)) or self.isStrPalindrome(s,(left+1),right)
            left+=1
            right-=1

        return True