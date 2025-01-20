class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        count=0
        vowels="aeiou"
        for i in range(len(word)):
            strs=word[i]
            for j in range(i+1 , len(word)):
                strs+=word[j]
                if ''.join(sorted(set(strs)))==vowels:
                    count+=1
        return count