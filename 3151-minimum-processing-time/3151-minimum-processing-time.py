class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        maxima=-inf
        l=0
        for i in processorTime:
            maxima=max(maxima , (i+(tasks[l])))
            l+=4
        return maxima
