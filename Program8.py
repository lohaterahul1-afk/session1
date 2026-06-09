#Armstrong Number
num=153
temp=num
sum=0
while num>0:
    digit=num%10
    sum+=digit**3
    num//=10
if temp==sum:
    print("is an armstrong number")
else:
    print("not an armstrong number")
