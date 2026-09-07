def morningSpendings():
    spending = float(input("Enter your morning spending: "))
    return spending


def afternoonSpendings():
    spending = float(input("Enter your afternoon spending: "))
    return spending


def eveningSpendings():
    spending = float(input("Enter your evening spending: "))
    return spending


def nightSpendings():
    spending = float(input("Enter your night spending: "))
    return spending


def totalSpendings():
    morning = morningSpendings()
    afternoon = afternoonSpendings()
    evening = eveningSpendings()
    night = nightSpendings()

    total = morning + afternoon + evening + night

    print("Total spending:", total)