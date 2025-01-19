class Solution:
    def countAndSay(self, n: int) -> str:
        hsh = {1: '1'}
        
        for i in range(2, n + 1):
            back = hsh[i - 1]
            r = l = 0
            strng = ""
            while r < len(back):
                count = 0   
                while r < len(back) and back[l] == back[r]:
                    count += 1
                    r += 1
                strng += str(count) + back[l]
                l = r
            hsh[i] = strng
        return hsh[n]
