import datetime
from django.conf import settings

def findRosterStartPoint():
    date1 = settings.GLOBAL_START_DATE
    one_day_delta = datetime.timedelta(days=1)
    today = datetime.date.today() + one_day_delta
    difference = today - date1
    # Convert difference from timedelta object to integer
    difference_int = difference.days
    
    while difference_int > 42:
        difference_int = difference_int % 42
        
    start_point_on_roster = difference_int
    
    return start_point_on_roster
    
def rosterPointerCheck(n):
    if n <= 42:
        return n
    else:
        n = 1
    return n