def chkpallindrome(num):
    temp = num 
    rev = 0
    while(temp > 0):
        d = temp %10
        rev = rev * 10 + d
        temp //= 10
    if(num==rev):
        return True
    else:
        return False
data =[123,545,7878,990,789987]
res = list(map(chkpallindrome , data))
print(res)        
