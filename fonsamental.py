import re

print("hello aissa")

name = "the GoodBye"

print(name)

print(name.upper())

print(name.lower())

print(name[0])

print(name[6])

print(name[0:3])

print(name[::2])

print(name[-1])

print(name[-4])

print(len(name))

text = "Royce "
text = text + "L-gang"

print(text)

print("hello royce\n how are you")

print("I learning programming \\ language")

print(r"I learning\ programming \" language")

print("I learning\t programming \" language")

txt = text.replace("L-gang" , "Issa")

print(txt)

height = "sorry Issa I am no here"

print(height.find("sorry"))

print(height.find("I"))

sub_list = height.split("I")

print(sub_list)

date = "2024-06-01"

date_list = date.split("-")
print(date_list)

test_re = "the this is a best day"

pattren = r"best"

match = re.search(pattren , test_re)

if match :
    print("it's found")
else:
    print("it's not found")
    
# digit \d number 0-9
# non-digit \D just caracters
# \w caracters a-z and A-Z and 0-9 
# \W  non-caracters !@#$%^&*
# \s space newline tab
# \S non-space non-newline non-tab
# \b word-boundary
# \B word-non=boundry

pattern = r"\d\d\d\d\d\d\d\d\d\d"

text = "my number phone is 0664336194"

match = re.search(pattern  , text)

if match :
    print("it's found :" , match.group())
else :
    print("it's not found")


patter = r"\W"

tet = "hello, what!@"

matcher = re.findall(patter , tet)

print("the list is :" , matcher)


s2 = "The BodyGuard is the best album of 'Whitney Houston'."

patt = r"Whitney Houston"

replacement = "legend"

new_string = re.sub(patt , replacement , s2 , flags=re.IGNORECASE)

print(new_string)