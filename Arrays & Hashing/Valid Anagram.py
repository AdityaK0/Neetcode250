def isAnagram(s: str, t: str):
    
    # the best and the most optimized way is using array as alphabets increase then decrease the char of both strings
    
    if len(t)!=len(s):
        return False
    
    count = [0]*26
    
    for i in range(len(s)):
        count[ord(s[i])-ord("a")]+=1
        count[ord(t[i])-ord("a")]-=1
    
    for ctn in count:
        if ctn>0:
            return False
    return True    
    
    # way 3 both string hash_map and compare thier key
    
    # s_hash_map = {}
    # best way is can be like this
    
    # for ch in s:
    #     s_hash_map[ch] = s_hash_map.get(ch,0)+1
    
    # for ch in t:
    #     s_hash_map[ch] = s_hash_map.get(ch,0)-1  
        
    # for key in s_hash_map:
    #     if s_hash_map[key]>0:
    #         return False
    
    # return True              
    
    # way 2 make t as a list and start remove each element which s have if character not found means False 
    
    # if len(s)!=len(t):
    #     return False
    
    # a = list(t)
    
    # for i in s:
    #     try:
    #         a.remove(i)
    #     except:
    #         return False
    # return True        
    
    # way1 o(log n)+o(log n)
    
    # s=sorted(s)
    # t=sorted(t)
    
    # return s==t




test_cases = [
    [ "racecar", "carrace"],
    ["jar","jam"],["xx","x"],
    ["a","aa"]
    
]

for test in test_cases:
    print(isAnagram(test[0],test[1]))