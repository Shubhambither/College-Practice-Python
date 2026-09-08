
def check(attendance):
   present=0
   absent=0
   for i in attendance:
       if(i=='P'):
        present=present+1 
       else:
        absent=absent+1
   if(present==6):
     print("Excellent attendance")
   elif(present==5 or present==4):
       print("Satisfactory Attendance")
   else:
       print("Poor attendace")   
list=[]
print("Enter attendance :\n")
for i in range(7):
  list.append(input(f"On day {i+1} : "))
  
check(list)

