class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        counter=0
        L=[]
        for x in seq:
            if x=="(":
                counter^=1
                L.append(counter)
            else:
                L.append(counter)
                counter^=1
        return L
        