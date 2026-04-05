def longestCommonPrefix(strs):
    for i in range(len(strs[0])):
        char = strs[0][i]

        for s in strs[1:]:
            if i >= len(s) or s[i] != char:
                return strs[0][:i]

    return strs[0].   #cant proceed



longestSubarray using hashmap and prefix sum 
isValid Skudo Optimal solution 
Prefix Suffix Playlist 


