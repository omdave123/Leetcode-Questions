class Solution:
    def dailyTemperatures(self, temp: list[int]) -> list[int]:
        n=len(temp)
        ans=[0]*n
        stack=[]
        for i in range (n):
            while stack and temp[stack[-1]]<temp[i]:
                j=stack.pop()
                ans[j]=i-j
            stack.append(i)
        return ans
        