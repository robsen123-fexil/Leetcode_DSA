class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def reverser(lsts):
            maxi=lsts[0]
            ind=0
            for i in range(1 , len(lsts)):
                if lsts[i]>maxi:
                    ind=i
                    maxi=lsts[i]
            print(lsts , lsts)
            res=lsts[:ind+1][::-1]+lsts[ind+1:]
           
            
            return [[ind+1 , len(res) ], res[::-1]]
        result=[]
        l=[]
        
        ans=[]
        l=0
        while sorted(arr)!=result:
            a , ll=reverser(arr)
            
            arr[:]=ll[:-1]
            ans.extend(a)
            
        return ans

