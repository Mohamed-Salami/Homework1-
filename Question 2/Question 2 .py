#first we using EXCEPTIONS \try-except\ to handle kind of errors 
#if users does not enter a Decimal Integer Value
try:
#using (input) method to let user input his Decimal Number          
    x=int(input("Enter your Decimal Number: "))
#Defined a empty list to put in it the binary value     
    your_binary_Number=[]
#using while loop in condition x>0 to calculate the binary number 
    while x>0  :
##Taking the remainder of the division by 2 ,And add the remainder to the empty list using (append) method
         your_binary_Number.append(x%2)
#Divide by 2 continues until the value 0 is reached and the loop exits         
         x=x//2
#using (reverse) method to reverse the list that contain the binary value of Decimal number
    your_binary_Number.reverse()
#Define an integer number to use loop to print list after reversing it  
    i=0 
    while i<len(your_binary_Number):
        print(your_binary_Number[i] , end="")
        i=i+1
#using except if users does not enter a Decimal Integer Value
except:
    print("ERROR.... DECIMAL INTEGER VALUE ONLY")        
