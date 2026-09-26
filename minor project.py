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
    mapfeel=[]
    satisfaction=[]
    mapsat=[]
    energy=[]
    mape=[]
    for row in range(8,44):
        value=ws.cell(row=row,column=11).value
        if value is not None:
            feeling.append(value)
    # print("Feeling",feeling)
    # print("Len of feeling",len(feeling))
    for feel in feeling:
        if feel=="Excellent":
            mapfeel.append(1)
        elif feel=="Good":
            mapfeel.append(2)
        elif feel=="Neutral":
            mapfeel.append(3)
        elif feel=="Low":
            mapfeel.append(4)
        elif feel =="Stressed":
            mapfeel.append(5)
    # print(mapfeel)
    # print("len of mapfeel",len(mapfeel))
    for row in range(8,44):
        value=ws.cell(row=row,column=12).value
        if value is not None:
            satisfaction.append(value)
    # print("Satis",satisfaction)
    # print("len of satis",len(satisfaction))
    for satis in satisfaction:
        if satis=="Very Satisfied":
            mapsat.append(1)
        elif satis=="Satisfied":
            mapsat.append(2)
        elif satis=="Neutral":
            mapsat.append(3)
        elif satis=="Unsatisfied":
            mapsat.append(4)
        elif satis =="Very Unsatisfied":
            mapsat.append(5)
    # print("mapsat",mapsat)
    # print("len of mapsat",len(mapsat))  
    for row in range(8,44):
        value=ws.cell(row=row,column=13).value
        if value is not None:
            energy.append(value)
    # print("energy",energy)
    # print("len of energy",len(energy))
    for e in energy:
        
        if e=='High':
            mape.append(1)
        elif e=='Medium':
            mape.append(2)
        elif e=='Low':
            mape.append(3)
      
    # print("mape",mape)
    # print("len of mape",len(mape))    
    return (math.fsum(mapfeel)+math.fsum(mapsat)+math.fsum(mape))/3

def data_continuity(sheet,expected_days):
    vrd=[]
    for row in range(8,44):
        value=ws.cell(row=row,column=1).value
        if value is not None:
            vrd.append(value) 
    return (len(vrd)*100/expected_days)  

wb = load_workbook('12603996.xlsx', data_only=True)
ws=wb["Daily Log"]

tpi=tech_productivity(ws)
print("Tech Productivity : ",tpi)
aai=academic_activity(ws)
print("Academic Activity : ",aai)
phai=physical_activity(ws)
print("Physical_activity : ",phai)
sri=sleep_recovery(ws)
print("Sleep & Recovery : ",sri)

print("Free/Unaccounted : ",activity_balance(ws))
tui=time_utilization(ws)
print("Time Utilization : ",tui)
ei=experience_index(ws)
print("Experience : ",ei)
dci=data_continuity(ws,36)
print("Data Contiuity : ",dci)

pai=0.15*tpi+0.20*aai+0.15*phai+0.20*sri+0.15*tui+0.10*ei+0.05*dci
print("Personal Activity Index = ",pai)
