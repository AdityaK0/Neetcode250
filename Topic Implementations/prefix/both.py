
arr = [3,2,1,42,21,12]

prefix = [0]*len(arr)
suffix = [0]*len(arr)
prefix[0] = 0
suffix[-1] = 0


for i in range(1,len(arr)): 
    prefix[i] = prefix[i-1]+arr[i-1]

for i in range(len(arr)-2,-1,-1):
    suffix[i] = suffix[i+1]+arr[i+1]

print(prefix)
print(suffix)    

print(sum(arr))

# at each index of both suffix and prefix if we add both prefix and suffix then add the arr of the same index it will always 
#return us the sum of the array 
