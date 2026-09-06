class Solution:
    def counter(self,s,t,i,j):
        if j == len(t):
            return 1
        if i == len(s):
            return 0
        if (i,j) in self.d:
            return self.d[(i,j)]
        
        if s[i] == t[j]:
            #2 choice skip or use
            skip=self.counter(s,t,i+1,j)
            use=self.counter(s,t,i+1,j+1)
            self.d[(i,j)]=skip+use
        else:
            self.d[(i,j)]=self.counter(s,t,i+1,j)
        return self.d[(i,j)]
    def numDistinct(self, s: str, t: str) -> int:
        self.d={}
        return self.counter(s,t,0,0)