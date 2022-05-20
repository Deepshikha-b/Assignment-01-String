str = input("Enter the statement: ") 
str = str.title()
str = str.split()
var = ""          #Empty string declaration     
for i in str:
    var = var + i[:-1] + i[-1].upper() + " "
print("Output statement is: ", var)
     