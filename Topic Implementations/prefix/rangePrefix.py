arr = [3, 1, 4, 8, 6, 2, 7, 5]

prefix = [0]*len(arr)

prefix[0] = 3 #as question say inclusive

for i in range(1,len(arr)):
    prefix[i] = prefix[i-1]+arr[i]


test = [
    (0, 3),
(2, 5),
(1, 6),
(4, 7),
(3, 3),
]   

for t in test:
    if t[0]==0:
        print(prefix[t[1]])
    else:    
      print(prefix[t[1]]-prefix[t[0]-1])
    # print(prefix[prefix[t[1]]] - prefix[prefix[t[0]]])