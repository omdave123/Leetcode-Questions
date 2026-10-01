class Solution:
    def isValid(self, s: str) -> bool:
        bracket=[]
        for x in s:
            if x in "({[":
                bracket.append(x)
            else:
                if not bracket:
                    return False
                k=bracket.pop()
                if k!="{" and x=="}":
                    return False
                if k!="(" and x==")":
                    return False
                if k!="[" and x=="]":
                    return False
        return not(len(bracket))