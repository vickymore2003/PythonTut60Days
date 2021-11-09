str = ' Hello world '

print(len(str))
print(str.lower())
print(str.upper())
print(str.capitalize())
print(str.count("l"))
print(str.strip())
print(str.replace("l","L"))
print(str.split(" "))
str1 = "Hello how are you"
x= "how" in str1
print(x)
x= "how" not in str1
print(x)
str3 = str+" " +str1
print((str3))
a = 23
b = "your are age is {}"
print(b.format(a))