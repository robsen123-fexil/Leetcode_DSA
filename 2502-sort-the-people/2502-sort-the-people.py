class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # for i in range(len(heights)):
        #     swp=False
        #     for j in range(len(heights)-i-1):
        #         if heights[j]>heights[j+1]:
        #             heights[j] , heights[j+1]=heights[j+1] , heights[j]
        #             swp=True
        #         if not swp:
        #             break
        # print(heights)
        for i in range(len(heights)):
            mini=i
            for j in range(i+1 , len(heights)):
                if heights[j]<heights[mini]:
                    mini=j
            heights[i] , heights[mini]=heights[mini] , heights[i]
            names[i] , names[mini]=names[mini] , names[i]
        return names[::-1]