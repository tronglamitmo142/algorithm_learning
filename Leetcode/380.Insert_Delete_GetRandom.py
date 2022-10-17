class RandomizedSet:
    def __init__(self):
        self.store = {}
    def insert(self, val):
        if val not in self.store:
            self.store[val] = 1
            return True
        else:
            self.store[val] += 1
            return False
    def remove(self, val):
        if val in self.store.keys():
            del self.store[val]
            return True
        else:
            return False 
    def getRandom(self):
        return random.choice(list(self.store.keys()))
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()