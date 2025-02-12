class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hsh=defaultdict(list)
        l=0
        r=len(numbers)-1
        while l<r:
            sums=numbers[l]+numbers[r]
            if sums==target:

                hsh[sums].extend([l+1 , r+1])
                l+=1
                r-=1
            elif sums>target:
                r-=1
            else:
                l+=1
        k=max(hsh.keys())
        return hsh[k]