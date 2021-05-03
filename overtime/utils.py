import datetime
from clocking.models import Quarter
from account.models import Account

def getCurrentQtr():
    '''
    Helper function to identify the current quarter.
    '''
    today = datetime.date.today()
    current_qtr = Quarter.objects.get(qtr_start_date__lte=today, qtr_end_date__gte=today)
    return current_qtr
    
def getNextQtr():
    '''
    Helper function to identify the next quarter.
    '''
    t = getCurrentQtr()
    t_end = t.qtr_end_date
    one_day_delta = datetime.timedelta(days=1)
    n = t_end + one_day_delta
    nextQtr = Quarter.objects.get(qtr_start_date=n)
    return nextQtr
    
def getQtrDateIn(n):
    '''
    Helper function to identify the quartera particular date is in.
    '''
    date_of_application = n
    qtr_date_in = Quarter.objects.get(qtr_start_date__lte=date_of_application, qtr_end_date__gte=date_of_application)
    return qtr_date_in
    
def getOfficerInstance(officer):
    '''
    Helper function to get account instance of officer from string.
    '''
    list_to_get_officer = officer.split()
    officer_instance = Account.objects.get(firstname=list_to_get_officer[0], lastname=list_to_get_officer[1])
    return officer_instance