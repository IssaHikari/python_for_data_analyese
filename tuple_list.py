tuple1 = (1 , 4, 3, 4, 5)

tuple2 = ("issa" , 20 , 1.90)

print(tuple2[0])

print(tuple2[-1])

tuple3 = ("royce" , 21 , 1.70)

tup = tuple2 + tuple3

print(tup)

subtup = tup[3:]

print(subtup)

print(len(tup))

sorttup = sorted(tuple1)

print(sorttup)

t = ('aissa' , ("issa" , 20) , 20 , 1.90)

print(t[1][0])


list1 = [1 , 'aissa' , ("Issa" , 20)]

print(list1[0])

print(list1[-1])

print(list1[0:2])

list2 = ["aaaa" , 20]

list1.extend(list2)

print(list1)

list1.append(["yyyy" , 3])

print(list1)

li = ["moussa" , 1945]

li[0] = "hakima"

print(li)

del(li[0])

print(li)

inn = "hikaro Issa".split()
print(inn)

A = ["banana" , 4]
B = A
B[0] = "Fruits"
print(A)
print(B)

C = A[:]

print(C)

C[0] = "vegituble"

print(A)
print(C)
#help(A)
