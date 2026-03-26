
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
            ""
    
    return prefix        

    #another way        ---------------- 0(n*m) Sc-0(1)
    
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


