# n=int(input("enter num"))
# for i in range(n):
#     for j in range(n):
#         print('*',end=' ')
#     print()
    

n=int(input("enter num"))
for i in range(n):
    for j in range(i+1):
        print('*',end=' ')
    print()
    

# n=int(input("enter num"))
# for i in range(n):
#     for j in range(i,n):
#         print('*',end=' ')
#     print()
        

# n=int(input("enter num"))
# for i in range(n):
#     for j in range(i+1):
#         print('*',end=' ')
#     print()
# for i in range(n):
#     for j in range(i,n):
#         print('*',end=' ')
#     print()


# n=int(input("enter num"))
# for i in range(n):
#     for j in range(n):
#         if(j==0 or j==n-1 or i==n-1):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n=int(input("enter num"))
# for i in range(n):
#     for j in range(n):
#         if(i==n//2 or j==n//2):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()        

# n=int(input("enter num"))
# for i in range(n):
#     for j in range(n):
#         if(i==j or i+j==n-1):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print() 


# n=int(input("enter num"))
# for i in range(n):
#     for j in range(n):
#         if(i==0 or j==0 or i==n-1 or j==n-1):
#             print("*", end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n=int(input("enter num"))
# for i in range(n):
#     for j in range(n):
#         if(j==0 or i==n-1 or i==j):
#             print("*", end=" ")
#         else:
            # print(" ",end=" ")
    # print()


# n=int(input("enter num"))
# for i in range(n):
#     for j in range(n):
#         if(j==0 or i==0 or i+j==n-1):
#             print("*", end=" ")
#         else:
#             print(" ",end=" ")
#     print()


n=int(input("enter num"))
for i in range (n):
    for j in range (i,n):
        print(" ",end=" ")
    for j in range (i):
        if(j==0 or i==n-1):
            print('*',end=' ')
        else:
            print(' ',end=' ')   
    for j in range(i+1):
        if(i==n-1 or i==j):
            print('*',end=' ')
        else:
            print(' ',end=' ')  
    print()        
                
# n=int(input("enter num"))
# for i in range(n):
#     for j in range(i,n):
#         print(' ',end=' ')
#     for j in range(i):
#         if(i==n-1 or j==0):
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     for j in range(i+1):
#         if(i==n-1 or i==j):
#              print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()


# def func(a):
#     a = a + 10
#     return a
# a = 5
# func(a)
# print(a)

             
# n=int(input("enter num"))
# x=1
# for i in range(n):
#     for j in range(i+1):
#         print(x,end=' ')
#     x+=1
#     print()

# n=int(input("enter num"))
# x=5
# for i in range(n):
#     for j in range(i+1):
#         print(x,end=' ')
#     x-=1
#     print()

# n=int(input("enter num"))
# x=1
# for i in range(n):
#     for j in range(i+1):
#         print(x,end=' ')
#     x+=1
#     print()
# x=5
# for i in range(n):
#     for j in range(i,n):
#         print(x,end=' ')
#     x-=1
#     print()

# n=int(input('enter num'))
# x=0
# for i in range(n):
#     for j in range(i+1):
#         print(x,end=" ")
#     x+=2
#     print()   

# n=int(input('enter num'))
# x=0
# for i in range(n):
#     for j in range(i+1):
#         if(i%2==0):
#             print('1',end=' ')
#         else:
#             print('2',end=' ')
#     print()   


# def is_armstrong_number(number:int)->bool:
#     num_str=str(number)
#     num_digits=len(num_str)
#     armstrong_sum=0
#     for digit in num_str:
#         armstrong_sum+=int(digit)**num_digits
#     return armstrong_sum==number
# num=int(input("enter a number:"))
# if is_armstrong_number(num):
#     print(f"{num} is an armstrong number")
# else:
#     print(f"{num} is not armstrong number")

# n=int(input("enter the value of n: "))
# s=0
# for i in range(1,n+1):
#     s=s+pow(i,3)
# print(s)

# x=int(input("Enter the lower limit for the range:"))
# y=int(input("Enter the upper limit for the range:"))
# for i in range(x,y+1):
#     if(i%2!=0):	
        # print(i)




    
        







