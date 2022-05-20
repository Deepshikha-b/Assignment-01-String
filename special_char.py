str = input("Enter the statement: ")         
symbols = {'~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/'}
str1 = set(str)                     # input converted to set
str1 = str1.intersection(symbols)
str_len = len(str1)
if str_len == 0:
    print("String is accepted") 
else:
    print("String is not accepted")

