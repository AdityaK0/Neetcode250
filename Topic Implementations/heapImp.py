# Elements must be comparable using <

# heapify up compares with parent
# heapify down compares with children nodes 

class Minheap:
    def __init__(self):
        self.heap = []
    
    def swap_(self,idx1,idx2):
        self.heap[idx1],self.heap[idx2] = self.heap[idx2],self.heap[idx1]
    
    
    def push(self,num):
        self.heap.append(num)
        self.heapify_up(len(self.heap)-1)
    
    def heapify_up(self,i):
        parent = (i-1)//2
        
        while i>0 and self.heap[parent]>self.heap[i]:
            self.swap_(i,parent)
            
            i = parent
            parent = (i-1)//2
    
    
    def pop(self):
        min_value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify_down(0)
        return min_value    
    
    def heapify_down(self,i):
        n = len(self.heap)
        
        while True:
            left = 2*i+1
            right = 2*i+2
            smallest = i
            if left<n and self.heap[left]<self.heap[smallest]:
                smallest = left
            
            if right<n and self.heap[right]<self.heap[smallest]:
                smallest = right
            
            if smallest == i:
                break
            
            self.swap_(smallest,i)
            
            i = smallest
               

heap1 = Minheap()

nums = [16,5,7,10,12,1]

heap1.push(nums[0])
heap1.push(nums[1])

for num in nums:
    heap1.push(num)
    
print(heap1.pop())
print(heap1.pop())
print(heap1.pop())

print(heap1.heap)

print(heap1.pop())