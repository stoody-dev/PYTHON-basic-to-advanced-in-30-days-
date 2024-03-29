#operations on strings 

a = "stoody"
print (len(a))

print(a.upper())
print(a.lower())

#strings are immmutable . Isme upper aur lower se strings me koi change nahi ayega . basically a change nahi hota . new string ban jaati hai string methods se 


str2 = "helloooo!!!"
print (str2.strip("!"))#remove only trailing characters . 

print(a.replace("stoody" ,"sawoo"))
print(a.split("o"))

print(len(a.center(12)))

print(a.endswith("y"))#checks if the string ends with a particular character 

b = "welcome to the jungle"
print(b.endswith("to",4,10))
print(a.find("o"))# searches for the 1st occurence and returns its index .

print(a.index("o"))