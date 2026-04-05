
arr = [3,2,1,42,21,12]

prefix = [0]*len(arr)

prefix[0] = 0

# for i in range(2,len(arr)):
#     curr_sum = 0
#     for j in range(i):
#         curr_sum+=arr[j]
#     prefix[i] = curr_sum    


# trying to find the prefix in 0(n) 

for i in range(1,len(arr)): 
    prefix[i] = prefix[i-1]+arr[i-1]

print(arr)
print(prefix)