class Solution(object):
    def generateParenthesis(self, n):
        S=[]
        def maze(p,open,close):
            if open+close==n*2:
                S.append(p)
                return
            if open<n:
                maze(p+"(",open+1,close)
            if close<open:
                maze(p+")",open,close+1)
        maze("",0,0)
        return S
        """
        :type n: int
        :rtype: List[str]
        """
        