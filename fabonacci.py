n=int(input('enter a num'))
a=0
b=1
c=0
if n==0 or n==1:
    print('num is fibonacci')
else:
    print('generating fabonacci series')
while c<n:
    print(a)
    c=a+b
    a=b
    b=c
    c+=1
