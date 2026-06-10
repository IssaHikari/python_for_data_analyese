coleur = ["red" , "orange" , "black" , "pink"]

for i in range(len(coleur)):
    coleur[i] = "white"


print(coleur)

for sequre in coleur:
    print(sequre)

for i,sequre in enumerate(coleur):
    print(f"{i} - {sequre}")

# while looops

listq = ["orange" , "orange" , "blue" , "orange"]

new_list = []

i = 0

while (listq[i] == "orange"):
    new_list.append(listq[i])
    i+=1

print(new_list)

