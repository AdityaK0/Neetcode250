import heapq
from collections import Counter
from operator import le

def topKFrequent(nums,k):
    # count each number frequency then sort the value in descending order then iterate over the hash_map till k 
    
    # using bucket_sort 
    
    # bucket = [ [] for _ in range(len(nums)+1) ]
    # # why list of empty bucket we can use simpl array also right but not what if the freq of 2 element are same then 
    # # they are also the k frequent this can be issue so lets say 3 and 4 both freq is 5 so it will store under same array
    
    # freq_map = Counter(nums)
    
    # for key in freq_map:
    #     bucket[freq_map[key]].append(key)
    
    # res = []
    
    # for i in range(len(bucket)-1,-1,-1):
    #     for key in bucket[i]:
    #         if len(res)==k:
    #             return res 
    #         res.append(key) 
            

    # return res 
    # count_freq = {}
    # heap = []
    
    # for num in nums:
    #     count_freq[num] = count_freq.get(num,0)+1
    
    # for num in count_freq:
        
    #     heapq.heappush(heap,(count_freq[num],num))
        
    #     if len(heap)>k:
    #         heapq.heappop(heap)
    
    # return [ heap_value[1] for heap_value in heap]        
    
    
    # using hash_map sort
    
    freq = Counter(nums)
    
    # return [key for key,val in freq.most_common()][:k]
    
    sorted_freq = sorted(freq.items(),key=lambda x:x[1],reverse=True)
    
    return [num for num,count in sorted_freq[:k]]
    

test_cases = [
    [[2,2,3,3,3,1,1,1,1],2],
    [[7,7],2]
]

for test_case in test_cases:
    print(topKFrequent(test_case[0],test_case[1]))