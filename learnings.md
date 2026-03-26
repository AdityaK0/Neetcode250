When two pointers are on the same array and you can't reuse elements — use low < high.
When two pointers are on two different arrays — low <= high is fine.

💡 Rule of Thumb
Use sorting first when:

You need to avoid duplicates
You are dealing with pairs/triplets
You want to use two pointers
Order of original array doesn't matter

When range is fixed with small range then we can use array as hash and update its index but if range is not fixed of 
element then better approch is to use us hashmap