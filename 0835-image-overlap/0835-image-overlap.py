class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        A=[]
        B=[]
        n=len(img1)
        d={}
        for i in range (n):
            for j in range (n):
                if img1[i][j]==1:
                    A.append([i,j])
                if img2[i][j]==1:
                    B.append([i,j])
        for a in A:
            for b in B:
                rel=(a[0]-b[0],a[1]-b[1])
                d[rel]=d.get(rel,0)+1
        return max(d.values(),default=0)