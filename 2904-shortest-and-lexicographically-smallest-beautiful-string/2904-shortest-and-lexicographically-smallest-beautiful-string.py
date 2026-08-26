class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left=0
        one=0
        length=len(s)
        res=""
        for right in range (length):
            if s[right]=="1":
                one+=1
            while one>k:
                if s[left]=="1":
                    one-=1
                left+=1
            if one==k:
                while s[left]=="0":
                    left+=1
                t=s[left:right+1]
                if (not res or len(t)<len(res) or (len(t)==len(res) and t<res)):
                    res=t
        return res