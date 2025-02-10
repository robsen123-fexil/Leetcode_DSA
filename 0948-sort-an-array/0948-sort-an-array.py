class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(nums):
            if  len(nums) > 1:
                mid = len(nums) // 2
                left_array = nums[:len(nums)//2]
                right_array = nums[len(nums)//2:]
                merge_sort(left_array)
                merge_sort(right_array)
                i = j = k = 0
                while i < len(left_array) and j < len(right_array):
                    if left_array[i] <= right_array[j]:
                        nums[k] = left_array[i]
                        i += 1
                    else:
                        nums[k] = right_array[j]
                        j += 1
                    k += 1

                while i < len(left_array):
                    nums[k] = left_array[i]
                    i += 1
                    k += 1

                while j < len(right_array):
                    nums[k] = right_array[j]
                    j += 1
                    k += 1
                
            return nums

        return merge_sort(nums)