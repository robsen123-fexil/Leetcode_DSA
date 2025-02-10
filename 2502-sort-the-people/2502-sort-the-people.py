class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # # """----------BUBBLE SORT----------  """
       
       
        # for i in range(len(heights)):
        #     swp=False
        #     for j in range(len(heights)-i-1):
        #         if heights[j]>heights[j+1]:
        #             heights[j] , heights[j+1]=heights[j+1] , heights[j]
        #             names[j] , names[j+1]=names[j+1] , names[j]
        #             swp=True
        #     if not swp:
        #         break
                
      
        
        
        
         
        # # """"------------ SELECTION SORT-----------"""" 
        
        # for i in range(len(heights)):
        #     mini=i
        #     for j in range(i+1 , len(heights)):
        #         if heights[j]<heights[mini]:
        #             mini=j
        #     heights[i] , heights[mini]=heights[mini] , heights[i]
        #     names[i] , names[mini]=names[mini] , names[i]
        # return names[::-1]
   


        # # """-------------INSERTION SORT---------------""""
        # for i in range(1 , len(heights)):
        #     j=i
        #     while heights[j]>heights[j-1] and j>0:
        #         heights[j] , heights[j-1]=heights[j-1] , heights[j]
        #         names[j] , names[j-1] =names[j-1] , names[j]
        #         j-=1
        # return names[::1]


        # """"---------Counting SORT----------------"""
        hsh=defaultdict(list)
        for i in range(max(heights)+1):
            hsh[i].append(0)
        for a , b  in zip(heights , names):
            hsh[a][0]+=1
            hsh[a].append(b)
        ans=[]
       
        for k , v in hsh.items():
            if v[0]>=1:
                ans.append(v[1])
        return ans[::-1]
        

