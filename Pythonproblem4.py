# Asking user for a positive integer. then output the successive value.
# If current value is even, then it is divided by 2. If current value is odd, it is multiplied by 3 and 1 is added. If current value is 1, the program ends

num = int(input("Please enter a positive integer: "))
total = 0

while total != 1:

    if num %2 == 0:
        total = (num * 3 +1)
        print ( total )
        total += total
    else:
        total = (num / 2)
        print ( total )
        total += total

print ("total is now 1")