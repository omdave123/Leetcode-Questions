class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        maximum=[nums[0]]*n
        minimum=[nums[-1]]*n
        for i in range (1,n):
            maximum[i]=max(maximum[i-1],nums[i])
            minimum[n-i-1]=min(minimum[n-i],nums[n-i-1])
        for i in range (n):
            if maximum[i]-minimum[i]<=k:
                return i
        return -1