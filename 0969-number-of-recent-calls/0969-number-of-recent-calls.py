class RecentCounter:

    def __init__(self):
        self.lists=deque()
        

    def ping(self, t: int) -> int:
        
        while self.lists and self.lists[0]<t-3000:
            self.lists.popleft()
            
        self.lists.append(t)
        return len(self.lists)
    
        

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)