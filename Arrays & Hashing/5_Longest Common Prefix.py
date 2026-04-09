
from decimal import MIN_ETINY


def longestCommonPrefix(strs):
    
    #ideal way  --------------- 0(n*m) Sc-0(1)
    
    if len(strs)==1: 
        return strs[0]
    if not strs:
        return ""
    
    prefix = strs[0]
    
    for i in range(1,len(strs)):
        
        j = 0
        
        while j<len(strs[i]) and j<len(prefix) and strs[i][j] == prefix[j]:
            j+=1
        
        prefix = prefix[:j]
        
        if not prefix: # nothing matched then empty string 
            return ""
    
    return prefix        

    #another way        ---------------- 0(n*m2) Sc-0(1) but includes extra concatenation so space issue 
    
    # first = strs[0]
    # ans = ""
    # for i in range(1,len(strs)):
        
    #     for j in range(min(len(first),len(strs[i]))):
    #         if first[j] == strs[i][j]:
    #             ans+=strs[i][j]
    #         else:
    #             break
    #     first = ans
    #     ans = ""
    
    # return first                

    
    
    # own way  ---------------- 0(n*m) Sc-0(1)
    
    # fstr = strs[0]
    # mini = float("inf")
    
    
    
    # for i in range(1,len(strs)):
    #     cstr = strs[i]
    #     k = 0
    #     ctn = 0
    #     while k<len(fstr) and k<len(cstr):
    #         if fstr[k] == cstr[k]:
    #             k+=1
    #             ctn+=1
    #         else:
    #             mini = min(k,mini)
    #             break 
        
    #     mini = min(ctn,mini)    
    
    # return fstr[0:mini]        


print(longestCommonPrefix(["bat","bag","bank","band"]))
print(longestCommonPrefix(["dance","dag","danger","damage"]))
print(longestCommonPrefix(["abc","","abcd"]))
print(longestCommonPrefix(["neet","feet"]))
print(longestCommonPrefix(["interview","internet","internal","interval"]
))



# ### Solution 1 (Prefix Shrinking)

# TC - O(n * m)
# SC - O(1)

# Why
# Compare each string with current prefix. In worst case, each comparison checks up to m characters. No extra space used.

# ---

# ### Solution 2 (Build string with ans)

# TC - O(n * m²)
# SC - O(m)

# Why
# Same comparisons as above, but string concatenation (`ans += char`) is O(m) each time → makes it quadratic.

# ---

# ### Solution 3 (Min tracking approach)

# TC - O(n * m)
# SC - O(1)

# Why
# Tracks minimum matching length across strings. Works, but logic is more complex than needed.

# ---

# ### Solution 4 (Vertical Scanning)

# TC - O(n * m)
# SC - O(1)

# Why
# Check column-wise (character by character across all strings). Stops early on mismatch. Same complexity, cleaner logic.

# ---

# If algorithm reference needed:
# All above are variations of **string comparison / scanning**, no special algorithm like DP or binary search involved.
