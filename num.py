# n=int(input())
# rev_num=0
# digit=0
# while n>0:
#     digit=n%10
#     rev_num=rev_num*10+digit
#     n=n//10
# print(rev_num)

# a=int(input('enter a'))
# b=int(input('enter b'))
# c=a
# a=b
# b=c
# print(a)
# print(b)

# n=int(input('enter'))
# if(n>0):
#     print('num is +ive')
# elif(n==0):
#     print('num is 0')
# else:
#     print('num is -ive')    

# h=int(input('enter h'))
# b=int(input('enter b'))
# area=0.5*b*h
# print(area)

# a=int(input())
# f=a*1.8+32
# print(f)

# n=int(input('enter'))
# m=n
# digit=0
# rev_num=0
# while n>0:
#     digit=n%10
#     rev_num=rev_num*10+digit
#     n=n//10
# if(rev_num==m):
#     print('num is pallindrome')
# else:
#     print('num is not pallindrome')
# print(rev_num)

# n=int(input('enter'))
# if n>1:
#     for i in range(2,n):
#         if(n%i==0):
#             print(n,'it is not prime num')
#             break
#         else:
#              print(n,'it is prime')
#              break

n=int(input('enter'))
for i in range(n):
    for j in range(n):
        print('*',end=' ')
    print()




