#Prog05. startswith() check if the string beginning part matches the function parameter. Create a program that do the same functionality without using startswith() function.
#Create a function to replicate startswith()
def startswith_replicate(text, beginning):
    start = "x" + text
    if "x" + beginning in start:
        return True
    else:
        return False
#Utilize the created function
name = "MarxiusIvan"
call = startswith_replicate(name, "Marxius")
print(call)
