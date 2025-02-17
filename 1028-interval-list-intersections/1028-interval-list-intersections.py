class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result=[]
        l=r=0
        
        while l<len(firstList) and r<len(secondList):
            a , b = firstList[l]
            c,d=secondList[r]
            maxi=max(a , c)
            mini=min(b ,d)
            if maxi<=mini:
                result.append([maxi , mini])
            if b<d:
                l+=1
            else:
                r+=1
        return result


                
            
