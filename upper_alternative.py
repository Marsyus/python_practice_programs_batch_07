#Prog03. upper() converts all characters of the string into upper case. Create a program that do the same functionality without using upper() function.
#Create a function to replicate upper()
def upper_replicate(text):
    table = str.maketrans("abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    output = text.translate(table)
    return output
#Utilize the created function
name = "MarxiusIvan"
call = upper_replicate(name)
print(call)
