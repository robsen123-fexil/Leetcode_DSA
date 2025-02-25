class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        ls= [0]
        hsh={'a' , 'e' , 'i' , 'o' , 'u'}
        for i in words:
            if i[-1] in hsh and i[0] in hsh:
                ls.append(1)
            else:
                ls.append(0)
        ls=list(accumulate(ls))
        print(ls)
        ans=[]
        for a , b in queries:
           
            ans.append(ls[b+1]-ls[a])
        return ans