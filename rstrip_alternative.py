#Prog01. rstrip() remove the space characters at the end of the string. Create a program that do the same functionality without using rstrip() function.
#Create a function to replicate rstrip()
def rstrip_replicate(text):
    strip = True
    output = ""
    for i in text[::-1]:
        if strip and i == " ":
            continue
        else:
            strip = False
            output += i
    return output[::-1]
#Utilize the created function
name = "Marxius Ivan   "
call = rstrip_replicate(name)
print(call)
