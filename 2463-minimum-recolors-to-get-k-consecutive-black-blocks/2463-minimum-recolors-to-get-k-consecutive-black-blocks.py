class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        minima=0
        lsts=[1 if i == 'B' else 0 for i in blocks]
        frsts=sum(lsts[:k])
        minima=k-frsts
        print(lsts)
        l=0
        for i in range(k , len(lsts)):
            print(frsts)
            frsts+=lsts[i]
            frsts-=lsts[l]
            l+=1
            minima=min(minima , k-frsts)
        return minima
