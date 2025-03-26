class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
       

        def solver(l ,  nums):
            
            r=len(nums)-1
           
            while l<=r:
                mid=l+(r-l)//2
                if nums[mid]==target:
                    return True
                elif nums[mid]>target:
                    r=mid-1
                else:
                    l=mid+1
            return False
        for i in range(len(matrix)):
            lsts=matrix[i]
            if lsts[-1]>=target:
                print('here')
                return solver(0 , lsts)
        return False

        