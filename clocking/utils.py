from datetime import datetime
import datetime as dt
from django.conf import settings

def findRosterStartPoint():
    date1 = settings.GLOBAL_START_DATE
    one_day_delta = dt.timedelta(days=1)
    today = dt.date.today() + one_day_delta
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
    
def getStartPageForPagination(d):
    first_date_on_roster = d
    seven_day_delta = dt.timedelta(days=7)
    x_date = first_date_on_roster + seven_day_delta
    today = dt.date.today()
    page_counter = 1
    
    while today > x_date:
        page_counter += 1
        x_date = x_date + seven_day_delta
        
    page_to_begin = page_counter
    return page_to_begin