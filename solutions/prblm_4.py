def reverse(num):
    reverse = 0 
    while(num > 0 ):
        reverse = reverse * 10 + (num % 10)
        num//=10
    return reverse

def isPalindrome(num):
    return  num == reverse(num)
    
def large_palindrome_product():
    j = 1
    for i in range(999*999 , 100*100 , -1):
        print(j , i)
        if isPalindrome(i):
                return i
        j+=1
    


print(large_palindrome_product())