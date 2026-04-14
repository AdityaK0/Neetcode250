

# need to check if the string is palindrome or not 
# if not then is it possible if we remove any character from the string then it can become valid palindrome



def validPalindrome(s):
    
    # the best solution is onething is common that if both left and right indexed strings are 
    # same then they are valid palindrome candidate and if not means 
    # need to check to palindrome in remaining part only not whole string cause as we 
    # skip the left and right index means they are already valid
    
    l,r = 0,len(s)-1
    
    def isPalindrome(l,r):
        
        while l<r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        
        return True
        
    while l<r:
        
        if s[l] == s[r]:
            l+=1
            r-=1
        
        else :
            return isPalindrome(l+1,r) or isPalindrome(l,r-1) 
    
    return True       
    
    
    
    # the below part we are taking extra space each time 0(n) 
    # then each time to get the reverse of the created string
    
    #TC - 0(n)2 SC - 0(n)2 
    # l,r = 0, len(s)-1
    
    # def s_without_given_index(index):
        
    #     c = ""
    #     for i in range(len(s)):
    #         if i==index:
    #             continue
    #         c+=s[i]
        
    #     return c    
            
    
    
    # while l<r:
    #     if s[l] == s[r]:
    #         l+=1
    #         r-=1
    #     else:
    #         skipL = s_without_given_index(l)
    #         skipR =  s_without_given_index(r)
    #         return skipL == skipL[::-1] or skipR == skipR[::-1]
        
    # return True   

print(validPalindrome("aba"))
print(validPalindrome("abbadc"))
print(validPalindrome("abbda"))
