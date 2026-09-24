class Solution:
    def digit_sum(self,n):
        res=0
        while n:
            res+=n%10
            n//=10
        return res
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i==self.digit_sum(nums[i]):
                return i
        return -1