


def firstOcuurence(haystack,needle):
    
    j=0
    for i in range(len(haystack)):
        
        current_idx = i
        
        while current_idx<len(haystack) and j<len(needle) and haystack[current_idx] == needle[j]:
            current_idx+=1
            j+=1
        
        if j == len(needle):
            return i
        j=0
    
    return -1    
                
        
        
haystack = "sacbutsad"
needle = "sad"

# haystack = "leetcode"
# needle = "leeto"

print(firstOcuurence(haystack,needle))   
    