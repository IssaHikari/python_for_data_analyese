dic = {"Thriller": 1900 , "Back in Black":1980 , "The Dark Side of the Moon": 1870 , "The Bodyguard": 1992}

print(dic["Back in Black"])

print(dic["The Dark Side of the Moon"])
dic["aissa"] = 2323

print(dic)

del(dic["aissa"])

print(dic)

if "Thriller" in dic:
    print("it's here")
else :
    print("it's not here")

print(dic.keys())

print(dic.values())