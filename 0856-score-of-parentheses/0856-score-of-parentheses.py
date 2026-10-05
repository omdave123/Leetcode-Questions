class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        total_count=0
        count=0
        for i in range(len(s)):
            if s[i]==")":
                count-=1
                if s[i-1]=="(":
                    total_count+=2**count
            else:
                count+=1
        return total_count