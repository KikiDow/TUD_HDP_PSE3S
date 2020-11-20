import datetime
from clocking.models import Quarter

def getCurrentQtr():
    today = datetime.date.today()
    current_qtr = Quarter.objects.get(qtr_start_date__lte=today, qtr_end_date__gte=today)
    return current_qtr
    
def getNextQtr():
    t = getCurrentQtr()
    t_end = t.qtr_end_date
    one_day_delta = datetime.timedelta(days=1)
    n = t_end + one_day_delta
    nextQtr = Quarter.objects.get(qtr_start_date=n)
    return nextQtr
    
def getQtrDateIn(n):
    date_of_application = n
    qtr_date_in = Quarter.objects.get(qtr_start_date__lte=date_of_application, qtr_end_date__gte=date_of_application)
    return qtr_date_in