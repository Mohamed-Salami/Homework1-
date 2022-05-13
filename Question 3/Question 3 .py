import json
#Define an empty dictionary that will be contain the   question of the exam  
exame_question={}
#using Input() to let user enter his name
student_name=input("Enter your full name: ")
#making first letter in each word of user name capital
#using strip to delete any spaces in the right or lift the full name
student_name=student_name.title()
student_name=student_name.strip()
#define an integer that indicate for mark user
mark=0
#open exm.json that we made it previously and put in it the questions and answers
#and we will treat "exam.json" as f
with open ("exam.json","r") as f :
#we put the content of exam.json in empty dictionary 
    exame_question=json.load(f)
print("welcome {} \n Your are going to answer of 20 Question about city capitals ".format(student_name))
#by for loop we are going through keys(the questions) of dictionary and print it then
#we let the user enter his answer 
for s in exame_question.keys():
    print(s)
    a=input("Enter your answer: ")
#using strip()to delete any spaces in right or left the answer 
#using title() for making agreement between the answer and values in first character
    a=a.strip()
#using if() condition to compare the right answer and the answer by the user 
    if a.title()==exame_question[s]:
#if the answer right we will add 1 to the mark and print true
#else the program print false 
        mark=mark + 1
        print("True")
    else:
        print("Fulse")
#Here using if() condition to evaluate the user based on his mark
if mark==20:
    print("Exellent \U0001F970 , {} you mark is {}".format(student_name,mark))
elif mark>15:
    print("Very Good \U0001F970, {} you mark is {}".format(student_name,mark))
elif mark >= 10:
    print("Good, {} you mark is {}".format(student_name,mark))
else:
    print("Sorry (\U0001F915 {} you mark is {} and You Failed".format(student_name,mark))   
#Here we are going to  creat a file and we will name it "Names.json" 
#and we will put the name of the user and his mark in it .
with open("Names.json","a") as t:
    mark=str(mark)
    student_name=student_name +" "+mark
    u=json.dump(student_name,t) 
    