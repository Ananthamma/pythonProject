

n=int(input('enter any number:'))

s= 0
t=n
while t>0:
    d=t%10
    s+=d**3
    t //=10

if n==s:
    print(n,'armstrong number')
else:
    print(n,'not armstrong number')