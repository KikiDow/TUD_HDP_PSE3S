{"filter":false,"title":"utils.py","tooltip":"/clocking/utils.py","undoManager":{"mark":8,"position":8,"stack":[[{"start":{"row":0,"column":0},"end":{"row":23,"column":12},"action":"insert","lines":["import datetime","from django.conf import settings","","def findRosterStartPoint():","    date1 = settings.GLOBAL_START_DATE","    one_day_delta = datetime.timedelta(days=1)","    today = datetime.date.today() + one_day_delta","    difference = today - date1","    # Convert difference from timedelta object to integer","    difference_int = difference.days","    ","    while difference_int > 42:","        difference_int = difference_int % 42","        ","    start_point_on_roster = difference_int","    ","    return start_point_on_roster","    ","def rosterPointerCheck(n):","    if n <= 42:","        return n","    else:","        n = 1","    return n"],"id":1}],[{"start":{"row":23,"column":12},"end":{"row":24,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":24,"column":0},"end":{"row":24,"column":4},"action":"insert","lines":["    "]},{"start":{"row":24,"column":4},"end":{"row":25,"column":0},"action":"insert","lines":["",""]},{"start":{"row":25,"column":0},"end":{"row":25,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":25,"column":0},"end":{"row":25,"column":4},"action":"remove","lines":["    "],"id":3}],[{"start":{"row":25,"column":0},"end":{"row":37,"column":24},"action":"insert","lines":["def getStartPageForPagination(d):","    first_date_on_roster = d","    seven_day_delta = dt.timedelta(days=7)","    x_date = first_date_on_roster + seven_day_delta","    today = dt.date.today()","    page_counter = 1","    ","    while today > x_date:","        page_counter += 1","        x_date = x_date + seven_day_delta","        ","    page_to_begin = page_counter","    return page_to_begin"],"id":4}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":15},"action":"remove","lines":["import datetime"],"id":5},{"start":{"row":0,"column":0},"end":{"row":1,"column":21},"action":"insert","lines":["from datetime import datetime","import datetime as dt"]}],[{"start":{"row":6,"column":27},"end":{"row":6,"column":28},"action":"remove","lines":["e"],"id":6},{"start":{"row":6,"column":26},"end":{"row":6,"column":27},"action":"remove","lines":["m"]},{"start":{"row":6,"column":25},"end":{"row":6,"column":26},"action":"remove","lines":["i"]},{"start":{"row":6,"column":24},"end":{"row":6,"column":25},"action":"remove","lines":["t"]},{"start":{"row":6,"column":23},"end":{"row":6,"column":24},"action":"remove","lines":["e"]},{"start":{"row":6,"column":22},"end":{"row":6,"column":23},"action":"remove","lines":["t"]},{"start":{"row":6,"column":21},"end":{"row":6,"column":22},"action":"remove","lines":["a"]}],[{"start":{"row":6,"column":21},"end":{"row":6,"column":22},"action":"insert","lines":["t"],"id":7}],[{"start":{"row":7,"column":19},"end":{"row":7,"column":20},"action":"remove","lines":["e"],"id":8},{"start":{"row":7,"column":18},"end":{"row":7,"column":19},"action":"remove","lines":["m"]},{"start":{"row":7,"column":17},"end":{"row":7,"column":18},"action":"remove","lines":["i"]},{"start":{"row":7,"column":16},"end":{"row":7,"column":17},"action":"remove","lines":["t"]},{"start":{"row":7,"column":15},"end":{"row":7,"column":16},"action":"remove","lines":["e"]},{"start":{"row":7,"column":14},"end":{"row":7,"column":15},"action":"remove","lines":["t"]},{"start":{"row":7,"column":13},"end":{"row":7,"column":14},"action":"remove","lines":["a"]},{"start":{"row":7,"column":12},"end":{"row":7,"column":13},"action":"remove","lines":["d"]}],[{"start":{"row":7,"column":12},"end":{"row":7,"column":13},"action":"insert","lines":["d"],"id":9},{"start":{"row":7,"column":13},"end":{"row":7,"column":14},"action":"insert","lines":["t"]}]]},"ace":{"folds":[],"scrolltop":179,"scrollleft":0,"selection":{"start":{"row":26,"column":4},"end":{"row":26,"column":29},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":3,"state":"start","mode":"ace/mode/python"}},"timestamp":1606404805622,"hash":"94b9edc8f1025e6dcb05dadd38150ff652d22ef1"}