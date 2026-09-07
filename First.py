marks1 = float(input("Enter marks in maths:"))
marks2 = float(input("Enter marks hindi:"))
marks3 = float(input("Enter marks english:"))
marks4 = float(input("Enter marks science:"))
marks5 = float(input("Enter marks punjabi:"))
total_marks=marks1+marks2+marks3+marks4+marks5
percentage = (total_marks/500)*100
print(percentage)
if(percentage>=90):
 print("Your grade is A+")
elif(percentage>=80 & percentage<90):
    print("Your grade is A")

elif(percentage>=70 & percentage<80):
    print("Your grade is B")

elif(percentage>=60 & percentage<70):
    print("Your grade is C")
elif(percentage>=50 & percentage<60):
    print("Your grade is D")
else:
 print("fail")
