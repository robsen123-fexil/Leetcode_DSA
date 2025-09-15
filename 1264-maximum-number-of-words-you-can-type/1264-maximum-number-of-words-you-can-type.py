class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        word=text.split()
        cnt=len(word)
        for i in word:
            for j in brokenLetters:
                if j in i:
                    cnt-=1
                    break
        return cnt
