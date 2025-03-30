#Prog02. removesuffix() remove the characters at the end of the string that matches the function parameter. Create a program that do the same functionality without using removesuffix() function.
#Create a function to replicate removesuffix()
def removesuffix_replicate(text, remove):
    if text.endswith(remove):
        output = text.replace(remove, "")
    else:
        output = text
    return output
#Utilize the created function
name = "MarxiusIvan"
call = removesuffix_replicate(name, "Ivan")
print(call)
