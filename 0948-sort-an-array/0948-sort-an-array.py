class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        result=[]
        def mergesort(nums , result):
            if len(nums)>1:
                mid=len(nums)//2
                lft=nums[:mid]
                rght=nums[mid:]
                mergesort(lft , result)
                mergesort(rght , result)
                i=j=k=0
                while i<len(lft) and j<len(rght):
                    if lft[i]<=rght[j]:
                        nums[k]=lft[i]
                        i+=1

                    elif lft[i]>=rght[j]:
                        nums[k]=rght[j]
                        j+=1
                    k+=1
                while i<len(lft):
                    nums[k]=lft[i]
                    i+=1
                    k+=1
                while j<len(rght):
                    nums[k]=rght[j]
                    j+=1
                    k+=1
            return nums
        return mergesort(nums , result)
                    
                