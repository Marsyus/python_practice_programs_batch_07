#Prog09. index() return the first location of the function parameter in the string. Create a program that do the same functionality without using index() function.
#Create a function to replicate index()
def index_replicate(val, var):
    first = True
    count = -1
    for i in var:
        if first:
            first_var = i
            first = False
    for i in val:
        if not first:
            count += 1
            if i == first_var:
                first = True
    return count
#Utilize the created function
name = "Marxius Ivan Adolf Denniel"
call = index_replicate(name, "l")
print(call)
