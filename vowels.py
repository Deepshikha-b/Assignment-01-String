str = input("Enter the statement: ") 
str = str.lower()
vowels = ('a','e','i','o','u')
count = 0
for i in str:
    if i in vowels:
       count += 1 
print(count)
