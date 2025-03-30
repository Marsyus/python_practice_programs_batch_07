#Prog07. zfill() add zero characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using zfill() function.
#Create a function to replicate zfill()
def zfill_replicate(num, width):
    need = width - len(num)
    output = "0" * need + num
    return output
#Utilize the created function
number = "0917"
call = zfill_replicate(number, 6)
print(call)
