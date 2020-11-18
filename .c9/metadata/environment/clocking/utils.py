{"filter":false,"title":"utils.py","tooltip":"/clocking/utils.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":23,"column":12},"action":"insert","lines":["import datetime","from django.conf import settings","","def findRosterStartPoint():","    date1 = settings.GLOBAL_START_DATE","    one_day_delta = datetime.timedelta(days=1)","    today = datetime.date.today() + one_day_delta","    difference = today - date1","    # Convert difference from timedelta object to integer","    difference_int = difference.days","    ","    while difference_int > 42:","        difference_int = difference_int % 42","        ","    start_point_on_roster = difference_int","    ","    return start_point_on_roster","    ","def rosterPointerCheck(n):","    if n <= 42:","        return n","    else:","        n = 1","    return n"],"id":1}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":23,"column":12},"end":{"row":23,"column":12},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":120,"mode":"ace/mode/python"}},"timestamp":1605541704118,"hash":"e1eda879d18f107814c7eacc7e897fcb1b367491"}