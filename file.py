A= [[1,2,3],
   [4,3,6],
   [7,8,7]]
b=[A[i][i] for i in range(len(A))] 
print(b)

# print('chitkara'+'a'+'b'+'c')

txt="i#am#fine"
x=txt.split("#")
print(x)

# def tuple_indexing(tup):
#     tup[1] = 800
#     return tup

# aTuple = (100, 800, 300, 400, 500)
# print(tuple_indexing(aTuple)(aTuple))



# l = [["a","b/","c"],["d","e","f"],["g","h","i"]]
# print (l[1:][1])

# l=["apple","mango","cherry","kiwi","apple"]
# l.reverse()
# print(l)

X = [[12,7],[4 ,5],[3 ,8]]
 
result = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]
for r in result:
  	    print(r)

# d1={"abc":5,"def":6,"ghi":7}
# print(d1["abc"])



