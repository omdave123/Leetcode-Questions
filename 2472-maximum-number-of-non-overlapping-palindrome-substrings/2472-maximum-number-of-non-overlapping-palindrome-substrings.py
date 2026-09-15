class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        def checker(left,right):
            while left<right:
                if s[right]!=s[left]:
                    return False
                right-=1
                left+=1
            return True
        n=len(s)
        res=0
        start=0
        for right in range (k-1,n):
            left=right-k+1
            if left>=start and checker(left,right):
                res+=1
                start=right+1
                continue
            left=right-k
            if left>=start and checker(left,right):
                res+=1
                start=right+1
        return res