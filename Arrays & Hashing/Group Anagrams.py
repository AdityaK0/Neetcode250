from collections import defaultdict
import re


def groupAnagrams(strs):
    if len(strs) == 1:
        return [ [strs[0]] ]  
    
    # more mature way
    
    # hash_map = defaultdict(list)
    hash_map = {}
    
    for s in strs:
        key = str(sorted(s))
        # hash_map[key].append(s) # it wont work directly if u dont use defaultdict will throw error if want to proceed
                                # without default dict then need condition if not then first have empty array
        
        if key not in hash_map:
            hash_map[key] = [] 
        
        hash_map[key].append(s)                  
    
    return [ value for value in hash_map.values()]    
    
    
    
    
    #dont know how but yes got accepted in leetcode 

    # hash_map = defaultdict(list)
    
    # for i in range(len(strs)):
    #     if not hash_map[str(sorted(strs[i]))]:
    
    ######### or instead of saving number just save the str directly
    
    #         hash_map[str(sorted(strs[i]))] = [strs[i]] 
    #     else:
    #         hash_map[str(sorted(strs[i]))].append(i)
    # return [ value for value in hash_map.values()] no need for below things
    # result = []
    # for key in hash_map:
    #     anagram_group = []
    #     for index in hash_map[key]:
    #         anagram_group.append(strs[index])
    #     result.append(anagram_group)  

    # return result         
            
    
    
    # result = [] tle came at 113th test case in leetcode 
    # already_checked = set()
    # for i in range(len(strings)):
    #     if str(sorted(strings[i])) not in already_checked:
            
        
    #         anagram_group = [strings[i]]
            
    #         for j in range(i+1,len(strings)):
                
    #             if sorted(strings[i]) == sorted(strings[j]):
    #                 anagram_group.append(strings[j]) 
    #                 already_checked.add(str(sorted(strings[j])))
                    
    #         result.append(anagram_group)
    
    # return result                         


print(groupAnagrams(["act","pots","tops","cat","stop","hat"]))
print(groupAnagrams(["x"]))
print(groupAnagrams([""]))



# [["hat"],["act", "cat"],["stop", "pots", "tops"]]