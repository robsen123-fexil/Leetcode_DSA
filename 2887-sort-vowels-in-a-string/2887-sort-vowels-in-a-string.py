class Solution:
    def sortVowels(self, s: str) -> str:
        res=""
        vow=[]
        vowels=['a' , 'e' , 'i' , 'o' , 'u' ,'A' , 'E' , 'I' , 'O' , 'U']
        for i in s:
            if i in vowels:
                vow.append(i)
        vow.sort()
        l=0
        for i in s:
            if i in vowels:
                res+=vow[l]
                l+=1
            else:
                res+=i
        return res
        