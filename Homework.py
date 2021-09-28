"""
Given an integer, n. perform the following conditional actions:
• If n is odd, print Weird
• If n is even and in the range 2 to 5. in not Weird
• If n is even and within the range 6 to 20. in Weird
• If n is even and greater than 20, print Not Weird
"""

#Initialize and assign the input value to the variable n
n = int(input('Nhap n: '))

#Use structure if-else to calculate

#If n is odd, print Weird
if n % 2 != 0:
    print('Weird')
#If n is event,we continue to compare the conditions
else:
    #If n range 2 to 5. in not Weird
    if (n>=2) and (n<=5):
        print('Not Weird')
    #If n within the range 6 to 20. in Weird
    if (n>=6) and (n<=20):
        print('Weird')
    #If n greater than 20, print Not Weird
    if n>20:
        print('Not Weird')



