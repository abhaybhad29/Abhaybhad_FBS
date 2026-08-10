def Sos(n):
    if(n>0):
        return n + Sos(n-1)
    else:
        return 0
n = 5
res = Sos(n)
print(res)    