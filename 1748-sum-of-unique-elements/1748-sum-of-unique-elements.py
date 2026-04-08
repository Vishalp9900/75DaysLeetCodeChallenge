class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        uniquesum=0
        dict={}
        for i in range(0,len(nums)):
            if nums[i] in dict:
                dict[nums[i]]+=1

            else:
                dict[nums[i]]=1

        for key , val in dict.items():
            if val==1:
                uniquesum+=key
        return uniquesum
        