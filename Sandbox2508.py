# create a fucntion to calculate the spendings of whole day
import spendings

def total_spendings(morning=spendings.morningSpendings(),afternoon=spendings.afternoonSpendings(),evening=spendings.eveningSpendings(),night=spendings.nightSpendings()):
    print(f'Morning spend is {morning}')
    print(f'Afternoon spend is {afternoon}')
    print(f'Evening spend is {evening}')
    print(f'Night spend is {night}')
    total_cal=morning+afternoon+evening+night
    return total_cal