import heapq

def topKFrequent(nums,k):
    # count each number frequency then sort the value in descending order then iterate over the hash_map till k 
    
    count_freq = {}
    heap = []
    
    for num in nums:
        count_freq[num] = count_freq.get(num,0)+1
    
    for num in count_freq:
        
        heapq.heappush(heap,(count_freq[num],num))
        
        if len(heap)>k:
            heapq.heappop(heap)
    
    return [ heap_value[1] for heap_value in heap]        
        


test_cases = [
    [[2,2,3,3,3,1,1,1,1],2],
    [[7,7],2]
]

for test_case in test_cases:
    print(topKFrequent(test_case[0],test_case[1]))