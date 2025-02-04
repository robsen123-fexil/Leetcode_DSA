class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result=[0]*(len(nums))
        print(result)
        for i in range(len(nums)):
            ind=(nums[i]+i )% len(nums)
            result[i]=nums[ind]
        return result
        #     if nums[i]>0:
        #         ind=((nums[i])+i)%len(nums)

        #         print(ind)
        #         result[i]=nums[ind]
        #     else:
        #         ind=(nums[i]+i)%len(nums)
        #         result[i]=nums[ind]
        # return result
            
