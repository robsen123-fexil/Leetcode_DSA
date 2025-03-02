class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        hsh={}
        for i in nums1:
            for j in range(len(i)):
                if i[j] in hsh:
                    hsh[i[j]]+=i[j+1]
                    break
                else:
                    hsh[i[j]]=i[j+1]
                    break
        for i in nums2:
            for j in range(len(i)):
                if i[j] in hsh:
                    hsh[i[j]]+=i[j+1]
                    break
                else:
                    hsh[i[j]]=i[j+1]
                    break
        result=[]
        for key, value in hsh.items():
            result.append([key  , value])
        result=sorted(result , key=lambda x:x[0])
        return result
                


        
        