class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives=0
        tens=0
        for i in bills:
            if i==5:
                fives+=1
            elif i==10:
                tens+=1
                if fives:
                    fives-=1
                else:
                    return False
               
            else:
                if tens and fives:
                    tens-=1
                    fives-=1
                else:
                    if fives>=3:
                       fives-=3
                    else:
                        return False
        return True if fives>=0 and tens>=0 else False
