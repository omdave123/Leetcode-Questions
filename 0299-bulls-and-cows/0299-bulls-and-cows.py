class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull=0
        cow=0
        d_secret={}
        d_guess={}
        for i in range (len(secret)):
            if secret[i]==guess[i]:
                bull+=1
            else:
                d_secret[secret[i]]=d_secret.get(secret[i],0)+1
                d_guess[guess[i]]=d_guess.get(guess[i],0)+1
        for x in d_secret:
            if x in d_guess:
                cow+=min(d_secret[x],d_guess[x])
        return (str(bull)+"A"+str(cow)+"B")