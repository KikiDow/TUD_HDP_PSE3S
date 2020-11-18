import datetime

def getCurrentYear():
    today = datetime.date.today()
    currentYear = today.year
    return currentYear
    
def roundMinutesToFifteenMinInterval(mins):
    base = 15
    if mins == 0.0 or mins == 15.0 or mins == 30.0 or mins == 45.0 or mins == 60.0:
        adjusted_mins = mins
    else:
        adjusted_mins = mins + 15.0
    rounded_mins = float(base * (adjusted_mins//base))
    return rounded_mins
    
def turnMinsToFractionOfHour(rounded_mins):
    fraction = float(rounded_mins/60)
    return fraction
    
def getLeaveAmount(time_delta):
    seconds = time_delta.seconds
    hours = float(seconds//3600)
    mins = float((seconds//60)%60)
    rounded_mins = roundMinutesToFifteenMinInterval(mins)
    if rounded_mins == 60.0:
        hours += 1.0
        mins = 0.0
        leave_amount = hours
    else:
        as_fraction_of_hour = turnMinsToFractionOfHour(rounded_mins)
        leave_amount = hours + as_fraction_of_hour
    return leave_amount