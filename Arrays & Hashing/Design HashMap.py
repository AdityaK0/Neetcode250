
class MyHashMap:
    def hash_key(self,key):
        return key%10000
    
    def __init__(self):
        self.map = [[] for i in range(10000)]
        

    def put(self, key: int, value: int):
        hashKey = self.hash_key(key)
        if not self.map[hashKey]:
            self.map[hashKey].append([key,value])
            return
        
        for k in range(len(self.map[hashKey])):
            if self.map[hashKey][k][0] == key:  
               self.map[hashKey][k][1] = value
               return 
        self.map[hashKey].append([key,value])
            
    def get(self, key: int):
        hashKey = self.hash_key(key)
        
        for k in range(len(self.map[hashKey])):
            if self.map[hashKey][k][0] == key:  
               return self.map[hashKey][k][1]
           
        return -1
    def remove(self, key: int):
        hashKey = self.hash_key(key)
        
        for k in range(len(self.map[hashKey])):
            if self.map[hashKey][k][0] == key:  
                self.map[hashKey].pop(k)
                return


actions = ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
actions_values = [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]


result = []

obj = MyHashMap()
result.append(None)
        
for i in range(1,len(actions)):
    
    if actions[i] == "put":
        result.append(obj.put(actions_values[i][0],actions_values[i][1]))
        
    elif actions[i] == "get":
        result.append(obj.get(actions_values[i][0]))
        
    elif actions[i] == "remove":
        result.append(obj.remove(actions_values[i][0]))       
print(result)
    