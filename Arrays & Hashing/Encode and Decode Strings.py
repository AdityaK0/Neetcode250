

def encode(strs):
    string = ""
    string_count = ""
    for s in strs:
        string_count+=str(len(s))
        string_count+="#"
        string+=s

    return string_count+"$"+string       

def decode(s):
    i = 0
    each_string_count = []
    
    count = ""
    while s[i]!="$":
        if s[i]=="#":
            each_string_count.append(int(count))
            count = ""
        else:
            count+=s[i]
        i+=1
    
    i = i+1 # as after $ we have our strings series
    
    res = []
    for string_count in each_string_count:
        temp_str = ""
        for k in range(i,string_count+i): # as to iterate till n need to go till n 
            temp_str+=s[k]
            i+=1
        res.append(temp_str)
            
    return res    
        
    
    

# def encode(strs):
#     count_of_each=""
    
    
#     for s in strs:
#         count_of_each+=str(len(s))+"#"
    
#     count_of_each+="$" # seprated each string count and all string 
    
#     for s in strs:
#         count_of_each+=s
    
#     return count_of_each    
        
    

# def decode(s):
#     strs_counts = []
#     i = 0
#     while s[i]!="$":
#         i+=1
    
#     temp = ""
#     for k in range(len(s[:i])):
#         if s[k]=="#":
#             strs_counts.append(int(temp))
#             temp = ""
#         else:
#             temp+=s[k]
    
#     i = i+1
    
#     res = []
#     for lengths in strs_counts:
#         ans = ""
#         for m in range(i,i+lengths):
#             ans+=s[m]
#             i+=1
#         res.append(ans)            
                
#     return res

# dummy_input = ["Hello","World","sec"]
dummy_input=["we","say",":","yes","!@#$%^&*()"]
print(encode(dummy_input))
print(decode(encode(dummy_input)))