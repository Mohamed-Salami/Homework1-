# Question 1 : -A- 
# first we define list that contain graduated student 
Gradute_Student=["Mohamed Salami","Ghadeer Bishani ","Roaa adnan","Maher Mansour","Karla kilani ","Rabee Ali "]
#we ask the student to input his first & last  name  
first_name= input ("Enter your first name ")
last_name = input("Enter your Last name ")
#using strip() to delete the spaces in the right & left strings to suitable the name in the last list 
fname=first_name.strip()
#using title() to make the first character in each of first & last name capital in in the last list
fname=fname.title()
lname=last_name.strip()
lname=lname.title()
# combining each of first_name & and last_name after modulating to use them like a full name for the students 
full_name= fname+" "+lname 
#making a condition to experment that the full name is belong to the last list or not
if full_name in Gradute_Student:    
    print("congratulations {} you graduated".format(full_name))
else:
    print("We are sorry for you \nGOOD LUCK  in the next year {}".format(full_name))
    
