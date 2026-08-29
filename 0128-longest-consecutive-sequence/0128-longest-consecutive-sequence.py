class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d=set(nums)
        counter_max=0
        for x in d:
            if x-1 not in d:
                counter=0
                while x in d:
                    counter+=1
                    x+=1
                counter_max=max(counter,counter_max)
        return counter_max
        