#print("hello")

#_he_llo="palak"
#print(_he_llo)

#fruits=["apple",'banana','grapes']
#x,y,z = fruits
#print(x)
#print(y)
#print(z)

#x="python "
#y="is "
#z="awesome "
#print(x +y +z)

#x=5
#y=5
#print(x+y)

#a='palak'
#b=1
#print(a,b)

#a= 'mental'
#def myfunc():
 #   print('palak is '+ a)
#myfunc()  


#def myfunc():
#   global x
# x='stupid'
#    print('she is ' + x)
#myfunc()
#print('he is '+ x)

#x='good'
#def myfunc():
#   global x
 #   x='great'
#myfunc()
#print('palak is '+ x)

# first_name= "tony "
# last_name= "stark"
# age= 51
# is_genius = True
# print(first_name + last_name)
# print(age)

# a=int(input())
# print("your age is",a)
# if(a>18):
     # print("you can drive")
# else:
     #  print('you cannot drive')    

# apple=180
# budget=200
# if(budget-apple>=100):
#     print("you can buy apples")
# elif(budget-apple>=30):
#     print("wait for few days")
# else:
#     print("don't buy")

# n=int(input("'enter num"))
# if(n<0):
#     print("num id negative")
# elif(n==0):
#     print("num is positive")
# elif(n>10 and n<=20):
#     print("num is b/w 11-20")
# else:
#     print("numm is greater than 20")   

     #    MATCH CASE
# date=int(input("enter nym b/w 1-7"))
# match date:
#    case 1:
     #    print("monday")
#    case 2:
     #    print("tuesday")
#    case 3:
     #    print("wednesday")
#    case 4:
     #    print("thrusday")        
#    case 5:
     #    print("friday")
#    case 6:
     #    print("saturday") 
#    case 7:
     #    print("sunday")
#    case _:
     #    print("invalid")

# for i in range(1,5,2):
#     print(i+1)

# i=5
# while i>=0:
#     print(i * "*") 
#     i=i-1   

# n=int(input("enter num"))
# m=int(input("enter num"))
# i=1
# while(i<=m):
#      print(n,"*",i,"=",n*i)
#      i=i+1
     
# sum=0
# n=int(input("enter"))
# i=1
# while(i<=n):
#     sum=sum+i
#     i=i+1
#     print(sum)
    
# for i in range(1,5):
#     for j in range(1,5):
#      print("*",end=" ")
# print()
    
# from math import factorial
# n=5
# for i in range(n):
#      for j in range(n-i+1):
#           print(end=" ")
#      for j in range(i+1):
#           print(factorial(i)//(factorial(j)*factorial(i-j)),end=" ")
#      print()


# rows=5
# b=0
# for i in range(rows,0,-1):
#      b+=1
#      for j in range(1,i+1):
#           print(b,end=" ")
#      print('\r')

# 
# str1=input("Enter the first String=") 
# str2=input("Enter the second String=") 
# for i in str1:     
#      for j in str2:         
#          if i==j: 
#             print(i) 

# string=input("Enter the Word=")
# count=0 
# for item in string:
#         if (item=='a' or item=='e' or item=='i' or item=='o' or item=='u'): 
#           count+=1 
# print("Number of vowels in the String are:",count)

# original_tuple = (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))  
# def is_element_present(element, tuple_of_tuples):
#      for inner_tuple in tuple_of_tuples:           
#          if element in inner_tuple:  
#              return True          
#          return False  
# element_to_check = 'White'  
# result = is_element_present(element_to_check, original_tuple)  
# print(f"Check if {element_to_check} present in the tuple of tuples: {result}") 


def print_file_in_reverse(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read lines from the file
            lines = file.readlines()

            # Print lines in reverse order
            for line in reversed(lines):
                print(line.strip())

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
# Example: Replace 'your_file.txt' with the path to your file
file_path = 'your_file.txt'
print_file_in_reverse(file_path)



