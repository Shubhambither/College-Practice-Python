import numpy as np
marks=np.array([ [85, 78, 92, 88],    [76, 89, 84, 91],    [90, 92, 88, 95],    [65, 70, 72, 68],    [88, 85, 90, 87]])
print(marks.shape)
print(marks.size)
total = np.sum(marks,axis=1)
# total = np.sum(marks)
average=np.sum(marks,axis=1)
print(average)
print("Highest marks :",np.max(marks,axis=1))
print("Lowest marks :",np.min(marks,axis=1))

print(total)