class Solution:
    def sumOfUnique(self, nums):
        from collections import Counter
        
        count = Counter(nums)
        total = 0
        
        for num in count:
            if count[num] == 1:
                total += num
                
        return total