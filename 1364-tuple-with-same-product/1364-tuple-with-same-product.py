class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        cnt=Counter()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                cnt[nums[i]*nums[j]]+=1
        count=0
        print(cnt)
        for v in cnt.values():
            if v>=2:
                count+=(v*(v-1)*4)
        return count
            