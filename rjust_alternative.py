#Prog06. rjust() add space characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using rjust() function.
#Create a function to replicate rjust()
def rjust_replicate(text, width, char=" "):
    output = char * width + text
    return output
#Utilize the created function
name = "Marxius"
call = rjust_replicate(name, 10)
print(call)
