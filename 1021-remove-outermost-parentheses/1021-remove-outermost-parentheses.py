class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res=[]
        count=0
        for x in s:
            if x==")":
                count-=1
            if count>0:
                res.append(x)
            if x=="(":
                count+=1
        return "".join(res)