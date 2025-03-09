class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        colors+=colors[:k-1]
        print(colors)
        l=count=0
        ls=[]
        if k==1:
            return len(colors)
        for i in range(1 , len(colors)):
            if colors[i]==colors[i-1]:
                l=i
                continue
            
            if i-l+1==k:
                count+=1
                l+=1
        return count

            

        return 0