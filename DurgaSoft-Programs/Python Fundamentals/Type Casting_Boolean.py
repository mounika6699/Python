#Converting Differnt data types into boolean
x=bool(62)
print("The boolean value of integer value 62 is:",x)
y=bool(22.5)
print("The boolean value of float number 22.5 is:",y)
print("The boolean value of float number 0.178 is:",bool(0.178))
print("The boolean value of float number 0.0 is:",bool(0.0))
print("The boolean value of complex number 10-2j:",bool(10-2j))
print("The booleam value of complex number 0+1.5j:",bool(0+1.5j))
print("The boolean value of complex number 0+0j:",bool(0+0j))
print('''The boolean value of string "True" is:''',bool("True"))
print('''The boolean value of string "False" is:''',bool("False"))
print("The boolean value of empty string is:",bool(""))