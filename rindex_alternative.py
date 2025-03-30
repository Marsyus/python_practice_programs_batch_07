#Prog10. rindex() return the first location of the function parameter in the string starting from the last character. Create a program that do the same functionality without using rindex() function.
#Create a function to replicate rindex()
def rindex_replicate(val, var):
    last = False
    count = len(val)
    for i in val[::-1]:
        if not last:
            count -= 1
            if i == var:
                last = True
    return count
#Utilize the created function
name = "Marxius Ivan Adolf Denniel"
call = rindex_replicate(name, "a")
print(call)
