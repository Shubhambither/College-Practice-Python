prizes=int(input("Enter total number of prizes : "))
students=int(input("Enter total number of students :"))

print("Prizes left after distribution are : " , prizes%students)
print("How many prizes will each student get : ", int(prizes/students))