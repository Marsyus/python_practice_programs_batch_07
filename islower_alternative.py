#Prog04. islower() check if all characters of the string is on lower case. Create a program that do the same functionality without using islower() function.
#Create a function to replicate islower()
def islower_replicate(text):
    lower_count = 0
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    for i in text:
        if i in lowercase:
            lower_count += 1
    if lower_count == len(text):
        return True
    else:
        return False
#Utilize the created function
name = "marxius"
call = islower_replicate(name)
print(call)
