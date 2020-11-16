{"filter":false,"title":"views.py","tooltip":"/clocking/views.py","undoManager":{"mark":25,"position":25,"stack":[[{"start":{"row":1,"column":0},"end":{"row":8,"column":34},"action":"insert","lines":["from django.shortcuts import render, redirect, get_object_or_404","from django.contrib.auth.decorators import login_required","from django.conf import settings","import datetime","from .models import Quarter, Shift, RosterSideA, RosterSideB, Roster","from django.contrib import messages","from.utils import findRosterStartPoint, rosterPointerCheck","from account.models import Account"],"id":2}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":35},"action":"remove","lines":["from django.shortcuts import render"],"id":3}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"remove","lines":["",""],"id":4}],[{"start":{"row":4,"column":0},"end":{"row":4,"column":1},"action":"insert","lines":["#"],"id":5}],[{"start":{"row":8,"column":25},"end":{"row":9,"column":0},"action":"insert","lines":["",""],"id":6},{"start":{"row":9,"column":0},"end":{"row":10,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":10,"column":0},"end":{"row":11,"column":47},"action":"insert","lines":["def landing_page(request):","    return render(request, \"landing_page.html\")"],"id":7}],[{"start":{"row":10,"column":26},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":8},{"start":{"row":11,"column":0},"end":{"row":11,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":11,"column":4},"end":{"row":11,"column":6},"action":"insert","lines":["''"],"id":9}],[{"start":{"row":11,"column":6},"end":{"row":11,"column":7},"action":"insert","lines":["'"],"id":10}],[{"start":{"row":11,"column":7},"end":{"row":12,"column":0},"action":"insert","lines":["",""],"id":11},{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"insert","lines":["    "]},{"start":{"row":12,"column":4},"end":{"row":13,"column":0},"action":"insert","lines":["",""]},{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":13,"column":4},"end":{"row":13,"column":5},"action":"insert","lines":["'"],"id":12},{"start":{"row":13,"column":5},"end":{"row":13,"column":6},"action":"insert","lines":["'"]},{"start":{"row":13,"column":6},"end":{"row":13,"column":7},"action":"insert","lines":["'"]}],[{"start":{"row":12,"column":4},"end":{"row":12,"column":5},"action":"insert","lines":["A"],"id":13}],[{"start":{"row":12,"column":5},"end":{"row":12,"column":6},"action":"insert","lines":[" "],"id":14},{"start":{"row":12,"column":6},"end":{"row":12,"column":7},"action":"insert","lines":["v"]},{"start":{"row":12,"column":7},"end":{"row":12,"column":8},"action":"insert","lines":["i"]},{"start":{"row":12,"column":8},"end":{"row":12,"column":9},"action":"insert","lines":["e"]},{"start":{"row":12,"column":9},"end":{"row":12,"column":10},"action":"insert","lines":["w"]}],[{"start":{"row":12,"column":10},"end":{"row":12,"column":11},"action":"insert","lines":[" "],"id":15},{"start":{"row":12,"column":11},"end":{"row":12,"column":12},"action":"insert","lines":["t"]},{"start":{"row":12,"column":12},"end":{"row":12,"column":13},"action":"insert","lines":["h"]},{"start":{"row":12,"column":13},"end":{"row":12,"column":14},"action":"insert","lines":["a"]},{"start":{"row":12,"column":14},"end":{"row":12,"column":15},"action":"insert","lines":["t"]}],[{"start":{"row":12,"column":15},"end":{"row":12,"column":16},"action":"insert","lines":[" "],"id":16},{"start":{"row":12,"column":16},"end":{"row":12,"column":17},"action":"insert","lines":["r"]},{"start":{"row":12,"column":17},"end":{"row":12,"column":18},"action":"insert","lines":["e"]},{"start":{"row":12,"column":18},"end":{"row":12,"column":19},"action":"insert","lines":["n"]},{"start":{"row":12,"column":19},"end":{"row":12,"column":20},"action":"insert","lines":["d"]},{"start":{"row":12,"column":20},"end":{"row":12,"column":21},"action":"insert","lines":["e"]},{"start":{"row":12,"column":21},"end":{"row":12,"column":22},"action":"insert","lines":["r"]},{"start":{"row":12,"column":22},"end":{"row":12,"column":23},"action":"insert","lines":["s"]}],[{"start":{"row":12,"column":23},"end":{"row":12,"column":24},"action":"insert","lines":[" "],"id":17},{"start":{"row":12,"column":24},"end":{"row":12,"column":25},"action":"insert","lines":["t"]},{"start":{"row":12,"column":25},"end":{"row":12,"column":26},"action":"insert","lines":["h"]},{"start":{"row":12,"column":26},"end":{"row":12,"column":27},"action":"insert","lines":["e"]}],[{"start":{"row":12,"column":27},"end":{"row":12,"column":28},"action":"insert","lines":[" "],"id":18},{"start":{"row":12,"column":28},"end":{"row":12,"column":29},"action":"insert","lines":["l"]},{"start":{"row":12,"column":29},"end":{"row":12,"column":30},"action":"insert","lines":["a"]},{"start":{"row":12,"column":30},"end":{"row":12,"column":31},"action":"insert","lines":["n"]},{"start":{"row":12,"column":31},"end":{"row":12,"column":32},"action":"insert","lines":["d"]},{"start":{"row":12,"column":32},"end":{"row":12,"column":33},"action":"insert","lines":["i"]},{"start":{"row":12,"column":33},"end":{"row":12,"column":34},"action":"insert","lines":["n"]}],[{"start":{"row":12,"column":34},"end":{"row":12,"column":35},"action":"insert","lines":["g"],"id":19}],[{"start":{"row":12,"column":35},"end":{"row":12,"column":36},"action":"insert","lines":[" "],"id":20},{"start":{"row":12,"column":36},"end":{"row":12,"column":37},"action":"insert","lines":["p"]},{"start":{"row":12,"column":37},"end":{"row":12,"column":38},"action":"insert","lines":["a"]},{"start":{"row":12,"column":38},"end":{"row":12,"column":39},"action":"insert","lines":["g"]},{"start":{"row":12,"column":39},"end":{"row":12,"column":40},"action":"insert","lines":["e"]}],[{"start":{"row":12,"column":40},"end":{"row":12,"column":41},"action":"insert","lines":[" "],"id":21},{"start":{"row":12,"column":41},"end":{"row":12,"column":42},"action":"insert","lines":["o"]},{"start":{"row":12,"column":42},"end":{"row":12,"column":43},"action":"insert","lines":["f"]}],[{"start":{"row":12,"column":43},"end":{"row":12,"column":44},"action":"insert","lines":[" "],"id":22},{"start":{"row":12,"column":44},"end":{"row":12,"column":45},"action":"insert","lines":["t"]},{"start":{"row":12,"column":45},"end":{"row":12,"column":46},"action":"insert","lines":["h"]}],[{"start":{"row":12,"column":46},"end":{"row":12,"column":47},"action":"insert","lines":[" "],"id":23},{"start":{"row":12,"column":47},"end":{"row":12,"column":48},"action":"insert","lines":["e"]}],[{"start":{"row":12,"column":47},"end":{"row":12,"column":48},"action":"remove","lines":["e"],"id":24},{"start":{"row":12,"column":46},"end":{"row":12,"column":47},"action":"remove","lines":[" "]}],[{"start":{"row":12,"column":46},"end":{"row":12,"column":47},"action":"insert","lines":["e"],"id":25}],[{"start":{"row":12,"column":47},"end":{"row":12,"column":48},"action":"insert","lines":[" "],"id":26},{"start":{"row":12,"column":48},"end":{"row":12,"column":49},"action":"insert","lines":["a"]},{"start":{"row":12,"column":49},"end":{"row":12,"column":50},"action":"insert","lines":["p"]},{"start":{"row":12,"column":50},"end":{"row":12,"column":51},"action":"insert","lines":["p"]},{"start":{"row":12,"column":51},"end":{"row":12,"column":52},"action":"insert","lines":["l"]},{"start":{"row":12,"column":52},"end":{"row":12,"column":53},"action":"insert","lines":["i"]},{"start":{"row":12,"column":53},"end":{"row":12,"column":54},"action":"insert","lines":["c"]},{"start":{"row":12,"column":54},"end":{"row":12,"column":55},"action":"insert","lines":["a"]},{"start":{"row":12,"column":55},"end":{"row":12,"column":56},"action":"insert","lines":["t"]},{"start":{"row":12,"column":56},"end":{"row":12,"column":57},"action":"insert","lines":["i"]}],[{"start":{"row":12,"column":57},"end":{"row":12,"column":58},"action":"insert","lines":["o"],"id":27},{"start":{"row":12,"column":58},"end":{"row":12,"column":59},"action":"insert","lines":["n"]},{"start":{"row":12,"column":59},"end":{"row":12,"column":60},"action":"insert","lines":["."]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":12,"column":60},"end":{"row":12,"column":60},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1605541843541,"hash":"e695daf2d287977d46194af16a1aaae8b01e0af2"}