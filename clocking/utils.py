from django.shortcuts import get_object_or_404
from datetime import datetime
import datetime as dt
from django.conf import settings
#from .models import Lates, LatesPerYear, Roster, Shift
from annual_leave.utils import getCurrentYear

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
    
def getSearchResultPaginationStartPage(ros_first_day, search_date):
    first_date_on_roster = ros_first_day
    seven_day_delta = dt.timedelta(days=7)
    x_date = first_date_on_roster + seven_day_delta
    key_date = search_date
    page_counter = 1
    
    while key_date > x_date:
        page_counter += 1
        x_date = x_date + seven_day_delta
        
    page_to_show = page_counter
    return page_to_show

def convertStrToDateObj(date_as_string):
    datetime_obj = datetime.strptime(date_as_string, "%d/%m/%Y")
    day = datetime_obj.day
    month = datetime_obj.month
    year = datetime_obj.year
    new_date = dt.date(year, month, day)
    return new_date
    
def checkForLateClocking(t, officer):
    from .models import Lates, LatesPerYear, Roster, Shift
    clocking_being_checked = t
    todays_date = dt.date.today()
    clocking_being_checked_as_dt_obj = dt.datetime.combine(todays_date, clocking_being_checked)
    
    person_who_clocked = officer
    todays_roster = Roster.objects.get(roster_officer_id=person_who_clocked, roster_shift_date=todays_date)
    #May add more conditional logic to check clocking for Overtime & Exchanges.
    todays_shift = get_object_or_404(Shift, pk=todays_roster.roster_shift.id)
    
    start_time_as_dt_obj = dt.datetime.combine(todays_roster.roster_shift_date, todays_shift.shift_start_time)
    
    if clocking_being_checked_as_dt_obj > start_time_as_dt_obj:
        late_duration = clocking_being_checked_as_dt_obj - start_time_as_dt_obj
        grace_period = dt.timedelta(minutes=10)
        if late_duration > grace_period:
            new_late = Lates(lates_officer_id=person_who_clocked, date_of_late=todays_roster.roster_shift_date, late_clocking_time=clocking_being_checked, duration_of_late=late_duration)
            new_late.save()
            #check for New Lates Per Year
            current_year = getCurrentYear()
            lates_for_current_year_check = LatesPerYear.objects.filter(yearly_lates_officer_id=person_who_clocked).filter(lates_year=current_year)
            if lates_for_current_year_check.exists():
                lates_for_current_year_check = LatesPerYear.objects.get(yearly_lates_officer_id=person_who_clocked, lates_year=current_year)
                lates_for_current_year_check.number_lates_for_year += 1
                lates_for_current_year_check.save()
            else:
                new_lates_for_current_year_check = LatesPerYear(yearly_lates_officer_id=person_who_clocked, lates_year=current_year, number_lates_for_year=1)
                new_lates_for_current_year_check.save()
    return
            
            
            
            
            
            
            