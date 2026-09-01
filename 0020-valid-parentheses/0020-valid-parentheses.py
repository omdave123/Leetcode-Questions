class Solution:
    def isValid(self, s: str) -> bool:
        bracket=[]
        for x in s:
            if x in "({[":
                bracket.append(x)
            else:
                if not bracket:
                    return False
                if bracket[-1]=="{" and x=="}":
                    bracket.pop()
                elif bracket[-1]=="(" and x==")":
                    bracket.pop()
                elif bracket[-1]=="[" and x=="]":
                    bracket.pop()
                else:
                    return False
        return not(len(bracket))