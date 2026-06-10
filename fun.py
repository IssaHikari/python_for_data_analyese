def add1(input):
    """
        add to input + 1
    """
    output = input + 1
    return output

def multi(input):
    output = input * 2
    return output

list1 = [1 , 2, 3, 4, 2, 6, 9, 8]

lenght = len(list1)
print(lenght)

S = sum(list1)
print(S)

new_sort = sorted(list1)

print(new_sort)
print(list1)

list1.sort()

print(list1)

help(add1)

def m(a ,b):
    c = a * b
    return c

t = m(2 , 3)
print(t)
text = m(2 , "aissa ")
print(text)

def M():
    print("aissa is the best")

M()

def P():
    pass

P()

def tab(baffer):
    for i,ba in enumerate(baffer):
        print(f"the index i:{i} and the value is : {ba}")

alboum = ["aissa" , "alph" , 20]

tab(alboum)

def name(*names):
    for nam in names:
        print(nam)
    
name("aissa" , "assia" , "chian")

# def golble(y):
#     x = x + "CD"
#     print(x)
#     return x

# x = "AB"

# z = golble(x)
# print(z)

# Python Program to Count words in a String using Dictionary
def freq(string):
    
    #step1: A list variable is declared and initialized to an empty list.
    words = []
    
    #step2: Break the string into list of words
    words = string.split() # or string.lower().split()
    
    #step3: Declare a dictionary
    Dict = {}
    
    #step4: Use for loop to iterate words and values to the dictionary
    for key in words:
        Dict[key] = words.count(key)
        
    #step5: Print the dictionary
    print("The Frequency of words is:",Dict)
    
#step6: Call function and pass string in it
freq("Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go")

def isGoodRating(rating=4): 
    if(rating < 7):
        print("this album sucks it's rating is",rating)
        
    else:
        print("this album is good its rating is",rating)

isGoodRating()
isGoodRating(10)

# Example of global variable

album = "The BodyGuard"
def printer1(album):
    internal_var1 = "Thriller"
    print(album, "is an album")
    
printer1(album )
# try runningthe following code
#printer1(internal_var1) 

album = "The BodyGuard"

def printer(album):
    global internal_var 
    internal_var= "Thriller"
    print(album,"is an album")

printer(album) 
printer(internal_var)

# Example of global variable

# myFavouriteBand = "AC/DC"

# def getBandRating(bandname):
#     if bandname == myFavouriteBand:
#         return 10.0
#     else:
#         return 0.0

# print("AC/DC's rating is:", getBandRating("AC/DC"))
# print("Deep Purple's rating is:",getBandRating("Deep Purple"))
# print("My favourite band is:", myFavouriteBand)

# # Deleting the variable "myFavouriteBand" from the previous example to demonstrate an example of a local variable 

# del myFavouriteBand

# # Example of local variable

# def getBandRating(bandname):
#     myFavouriteBand = "AC/DC"
#     if bandname == myFavouriteBand:
#         return 10.0
#     else:
#         return 0.0

# print("AC/DC's rating is: ", getBandRating("AC/DC"))
# print("Deep Purple's rating is: ", getBandRating("Deep Purple"))

# Example of global variable and local variable with the same name

myFavouriteBand = "AC/DC"

def getBandRating(bandname):
    myFavouriteBand = "Deep Purple"
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is:",getBandRating("AC/DC"))
print("Deep Purple's rating is: ",getBandRating("Deep Purple"))
print("My favourite band is:",myFavouriteBand)

def printAll(*args): # All the arguments are 'packed' into args which can be treated like a tuple
    print("No of arguments:", len(args)) 
    for argument in args:
        print(argument)
#printAll with 3 arguments
printAll('Horsefeather','Adonis','Bone')
#printAll with 4 arguments
printAll('Sidecar','Long Island','Mudslide','Carriage')


def printDictionary(**args):
    for key in args:
        print(key + " : " + args[key])

printDictionary(Country='Canada',Province='Ontario',City='Toronto')

def addItems(list):
    list.append("Three")
    list.append("Four")

myList = ["One","Two"]

addItems(myList)

print(myList)
