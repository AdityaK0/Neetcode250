arr = [3,2,1,42,21,12]
# arr = [1,2,3,4,5,6]

suffix = [0]*len(arr)

# for i in range(len(arr)):
#     curr_sum = 0
#     for j in range(i+1,len(arr)):
#         curr_sum+=arr[j]
    
#     suffix[i] = curr_sum

suffix[-1] = 0

# implement in  0(n)

for i in range(len(arr)-2,-1,-1):
    suffix[i] = suffix[i+1]+arr[i+1]

print(arr)
print(suffix)        
        

