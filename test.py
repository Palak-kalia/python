l1=list(int(x)for x in input().split())
print(l1)
l2=list(int(y)for y in input().split())
print(l2)
l3=[]
sum1=0
sum2=0
for i in l1[:9+1:+2]:
    sum1=sum1+i
l3.insert(0,sum1)

for j in l2[1:9+1:+2]:
    sum2=sum2+j
l3.insert(1,sum2)
print(l3)

for i in range(5):
    for s in range(i,5):
        print(' ',end='')


    for j in range(i+1):
        print(l3[0],end='')
    print()

for i in range(5):
    for s in range(i,5):
        print(' ',end='')

    for j in range(i+1):
        print(l3[1],end='')
    print()


# def odd(n):
#     for i in range(1, n+1):
#         print(" " * (n-i), str(n) * i)

# def even(n):
#     for i in range(1, n+1):
#         print(str(n) * i)


# n = int(input("Enter length:- "))
# l = list(int(x) for x in input().split())

# for j in range(1, n, 2):
#     odd(l[j])


# for j in range(0, n, 2):
#     even(l[j])







# l=[]
# n=int(input('enter n'))
# m=int(input('enter m'))
# for i in range(n):
#     l1=[]
#     for j in range(m):
#         x=int(input())
#         l1.append(x)
#     l.append(l1)

# for i in l:
#     print(i)
# li=[]
# n=int(input('enter n'))
# m=int(input('enter m'))
# for i in range(n):
#     l2=[]
#     for j in range(m):
#         y=int(input())
#         l2.append(y)
#     li.append(l2)

# for i in li:
#     print(i)

# lp=[]
# for i in range(n):
#     l3=[]
#     for j in range(m):
#         sum=l[i][j]+li[i][j]
#         l3.append(sum)
#     lp.append(l3)
#     # print(lp)
# for i in lp:
#     print(i)   
 

# s=input('enter string')
# upper_count=0
# lower_count=0
# digit=0
# space_count=0
# for i in s:
#     if(i.isupper()==True):
#         upper_count+=1
#     elif(i.islower()==True):
#         lower_count+=1
#     elif(i.isdigit()==True):
#         digit+=1
#     elif(i.isspace()==True):
#         space_count+=1
# print('upper_count is =',upper_count)
# print('lower_count is =',lower_count)
# print('digit is =',digit)
# print('space_count is =',space_count)







        


    
