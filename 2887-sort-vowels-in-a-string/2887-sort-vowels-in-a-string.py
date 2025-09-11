class Solution:
    def sortVowels(self, s: str) -> str:
        ans=""
        vowels=['a' , 'e' , 'i' , 'o' , 'u' , 'A' , 'E' , 'I' , 'O' , 'U' ]
        v=[]
        for i in s:
            if i in vowels:
                v.append(i)
        l=0
        v.sort()
        for i in s:
            if i in v:
                ans+=v[l]
                l+=1
            else:
                ans+=i
        return ans