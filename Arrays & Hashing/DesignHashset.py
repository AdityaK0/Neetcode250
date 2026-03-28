class ListNode:
    def __init__(self,key):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.set = [ ListNode(0) for _ in range(10001)]

    def add(self, key: int):
        index = key%10000
        curr = self.set[index]

        while curr.next:
            if curr.next.key == key:
                return
            curr = curr.next
        curr.next = ListNode(key)


    def remove(self, key: int):
        index = key%10000
        curr = self.set[index]

        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next    

    def contains(self, key: int):
        index = key%10000
        curr = self.set[index]

        while curr.next:
            if curr.next.key == key:
                return True
            curr = curr.next 
        return False    
        


# class MyHashSet:
    
    
#     # all takes 0(n) but at small scale of array and also memory efficient by bucket method and collision concept
#     # whatever key will be we will gonna divide that by 1000 and operate on that index while removing,adding or finding will iterate over that particular index array []
    
#     def __init__(self):
#         self.hashSet = [[] for _ in range(1000)]
    
#     def hash_key(self,key):
#         return key%1000
    
#     def add(self,key):
        
#         setArr = self.hashSet[self.hash_key(key)]
        
#         if not setArr:
#             self.hashSet[self.hash_key(key)].append(key)
#             return
#         if key not in setArr:
#             self.hashSet[self.hash_key(key)].append(key)
    
#     def remove(self,key):
#         setArr = self.hashSet[self.hash_key(key)]
#         for i in range(len(setArr)):
#             if setArr[i] == key:
#                self.hashSet[self.hash_key(key)].pop(i)
    
#     def contains(self,key):
#         setArr = self.hashSet[self.hash_key(key)]
#         if key in setArr:
#             return True
#         return False
           
        
    
    
    
    
    
    
#     # all operations take 0(1) but its memory ineficient is the key range in large
#     # MAX_SIZE = 10**6+1
#     # def __init__(self):
#     #     self.set = [False]*self.MAX_SIZE
    
#     # def add(self,key):
#     #     self.set[key] = True
    
#     # def remove(self,key):
#     #     self.set[key] = False
    
#     # def contains(self,key):
#     #     return self.set[key]             
    
        
    
    
    
#     # all operations takes 0(n)
    
#     # def __init__(self):
#     #     self.hashTable = []
    
#     # def add(self,val):
#     #     if not self.hashTable:
#     #         self.hashTable.append(val)
#     #     is_there = False 
#     #     for v in range(len(self.hashTable)):
#     #         if self.hashTable[v] == val:
#     #             is_there = True
#     #             break
        
#     #     if not is_there:
#     #         self.hashTable.append(val)
#     #     return None
    
#     # def remove(self,val):
#     #     for v in range(len(self.hashTable)):
#     #         if self.hashTable[v] == val:
#     #             self.hashTable.pop(v)
#     #     return False
    
#     # def contains(self,val):
#     #     for v in range(len(self.hashTable)):
            
#     #         if self.hashTable[v] == val:
                
#     #             return True
#     #     return False        

actions = ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
actions_values = [[], [1], [2], [1], [3], [2], [2], [2], [2]]



result = []

obj = MyHashSet()
result.append(None)
        
for i in range(1,len(actions)):
    
    if actions[i] == "add":
        result.append(obj.add(actions_values[i][0]))
        
    elif actions[i] == "contains":
        result.append(obj.contains(actions_values[i][0]))
        
    elif actions[i] == "remove":
        result.append(obj.remove(actions_values[i][0]))       

print(result)



