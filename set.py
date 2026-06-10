list_to_set = ['aissa' , 20  , "footbool" , 20.5  , 'aissa']

new_set = set(list_to_set)

print(list_to_set)
print(new_set)

new_set.add("royce")

print(new_set)

new_set.remove('aissa')

print(new_set)

if "aissa" in new_set:
    print("it's found")
else:
    print("it's not found")

set2 = {"footbool" , "royce" , 3 , 89}

n_set = new_set & set2

print(n_set)

nn_set = new_set.union(set2)

print(nn_set)

subset = {"footbool",3,  'royce'}

check = subset.issubset(nn_set)

print(nn_set)
print(subset)
if check:
    print("it's subset")
else :
    print("it's not subset")


diff = nn_set.difference(subset)
print(diff)

diff1 = subset.difference(nn_set)
print(diff1)

inter = nn_set.intersection(subset)

print(inter)

chec = nn_set.issuperset(subset)

if chec :
    print("it's the super")
else :
    print("it's not the super")
