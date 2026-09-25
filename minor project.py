from openpyxl import load_workbook
import math
def tech_productivity(sheet):
    values=[]
    for row in range(8,44):
        value=ws.cell(row=row,column=5).value
        if value is not None:
            values.append(value)  
    return math.fsum(values)/len(values)

def physical_activity(sheet):
    fitness=[]
    for row in range(8,44):
        value=ws.cell(row=row,column=3).value
        if value is not None:
            fitness.append(value) 
    return math.fsum(fitness)/len(fitness)
def sleep_recovery(sheet):
    sleep=[]
    for row in range(8,44):
        value=ws.cell(row=row,column=2).value
        if value is not None:
            sleep.append(value) 
    return math.fsum(sleep)/len(sleep)

def activity_balance(sheet):
    free=[]
    for row in range(8,44):
        value=ws.cell(row=row,column=10).value
        if value is not None:
            free.append(value) 
    return math.fsum(free)/len(free)
def time_utilization(sheet):
    time=[]
    for row in range(8,44):
        value=ws.cell(row=row,column=9).value
        if value is not None:
            time.append(value) 
    return math.fsum(time)/len(time)

def academic_activity(sheet):
    study=[]
    c=[]
    for row in range(8,44):
        value=ws.cell(row=row,column=4).value
        if value is not None:
            study.append(value)  
    for row in range(8,44):
        value=ws.cell(row=row,column=6).value
        if value is not None:
            c.append(value)  
    return (math.fsum(study)+math.fsum(c))/len(study)
def experience_index(sheet):
    feeling=[]
    satisfaction=[]
    energy=[]
    for row in range(8,44):
        value=ws.cell(row=row,column=11).value
        if value is not None:
            feeling.append(value)  
    for row in range(8,44):
        value=ws.cell(row=row,column=12).value
        if value is not None:
            satisfaction.append(value)  
    for row in range(8,44):
        value=ws.cell(row=row,column=13).value
        if value is not None:
            energy.append(value)  
    return (math.fsum(feeling)+math.fsum(satisfaction)+math.fsum(energy))/len(3*feeling)

wb = load_workbook('12603996.xlsx', data_only=True)
ws=wb["Daily Log"]
print("Tech Productivity : ",tech_productivity(ws))
print("Academic Activity : ",academic_activity(ws))
print("Physical_activity : ",physical_activity(ws))
print("Sleep & Recovery : ",sleep_recovery(ws))
print("Free/Unaccounted : ",activity_balance(ws))
print("Time Utilization : ",time_utilization(ws))
print("Experience : ",experience_index(ws))

