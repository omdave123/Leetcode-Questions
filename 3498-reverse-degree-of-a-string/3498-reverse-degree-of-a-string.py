class Solution:
    def reverseDegree(self, s: str) -> int:
        ans=0
        i=1
        for x in s:
            ans+=(123-ord(x))*i
            i+=1
        return ans
        