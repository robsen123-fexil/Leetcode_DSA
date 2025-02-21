class LRUCache:

    def __init__(self, capacity: int):
        self.hsh=defaultdict(int)
        self.cap=capacity
        self.lists=[]

    def get(self, key: int) -> int:
        if key in self.hsh:
            self.lists.remove(key)
            self.lists.append(key)
            return self.hsh[key]
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.hsh:
            self.lists.remove(key)
        elif len(self.hsh)>=self.cap:
            lrukey=self.lists.pop(0)
            del self.hsh[lrukey]
        self.hsh[key]=value
        self.lists.append(key)

        



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)