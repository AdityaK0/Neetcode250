

# Ideal way 

def encode(strs):
    string = ""
    for s in strs:
        string+=str(len(s))+"#"+s
    
    return string

def decode(s):
    i = 0
    res = []
    while i<len(s):
        j = i
        
        # why find till # got the doubt but then what length is 2 digits then 
        while s[j]!="#":
            j+=1
        
        length = int(s[i:j]) # as j will stop at # which means before that whatever digits we have is the string length
        
        i = j+1 # why this did cause at j we have # and after that we know we have the string it self so from there i to i+length    
        
        res.append(s[i:i+length])
        
        i = i+length
    
    return res    
        
# SC and TC both 0(m*n)

# def encode(strs):
#     string = ""
#     string_count = ""
#     for s in strs:
#         string_count+=str(len(s))
#         string_count+="#"
#         string+=s

#     return string_count+"$"+string       

# def decode(s):
#     i = 0
#     each_string_count = []
    
#     count = ""
#     while s[i]!="$":
#         if s[i]=="#":
#             each_string_count.append(int(count))
#             count = ""
#         else:
#             count+=s[i]
#         i+=1
    
#     i = i+1 # as after $ we have our strings series
    
#     res = []
#     for string_count in each_string_count:
#         temp_str = ""
#         for k in range(i,string_count+i): # as to iterate till n need to go till n 
#             temp_str+=s[k]
#             i+=1
#         res.append(temp_str)
            
#     return res    
        
dummy_input=["we","say",":","yes","!@#$%^&*()"]
print(encode(dummy_input))
print(decode(encode(dummy_input)))