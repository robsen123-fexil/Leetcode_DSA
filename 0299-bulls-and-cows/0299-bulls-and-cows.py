class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a =b =0
        visited=[]
        cnt1=Counter(secret)
        cnt2=Counter(guess)
        for k , v in cnt1.items():
            if cnt2[k]:
                b+=min(cnt2[k] , v)
        for i , j in zip(secret , guess):
            if i==j:
                a+=1
                b-=1
       
        return str(a)+'A'+str(b)+'B'
        