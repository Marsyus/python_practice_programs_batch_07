#Prog08. count() return how many time the function parameter appear in the string. Create a program that do the same functionality without using count() function.
#Create a function to replicate count()
def count_replicate(val, var):
    count = 0
    for i in val:
        if i == var:
            count += 1
    return count
#Utilize the created function
name = "Marxius Ivan Adolf Denniel"
call = count_replicate(name, "n")
print(call)
