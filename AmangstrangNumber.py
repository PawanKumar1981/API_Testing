#153 27+125+1
num=153
c=0
tempnum=num
while num>0:
    a=num%10
    c=c+(a*a*a)
    num//=10
print(c)



