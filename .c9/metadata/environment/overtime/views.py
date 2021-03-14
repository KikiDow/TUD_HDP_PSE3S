{"filter":false,"title":"views.py","tooltip":"/overtime/views.py","undoManager":{"mark":71,"position":71,"stack":[[{"start":{"row":425,"column":60},"end":{"row":426,"column":0},"action":"insert","lines":["",""],"id":290},{"start":{"row":426,"column":0},"end":{"row":426,"column":4},"action":"insert","lines":["    "]},{"start":{"row":426,"column":4},"end":{"row":427,"column":0},"action":"insert","lines":["",""]},{"start":{"row":427,"column":0},"end":{"row":427,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":427,"column":4},"end":{"row":437,"column":57},"action":"insert","lines":["#pagination for annual leave requests","    al_page_number = 1","    al_page = request.GET.get('al_page', al_page_number)","    ","    al_paginator = Paginator(my_annual_leave_requests, 2)","    try:","        my_al = al_paginator.page(al_page)","    except PageNotAnInteger:","        my_al = al_paginator.page(1)","    except EmptyPage:","        my_al = al_paginator.page(al_paginator.num_pages)"],"id":291}],[{"start":{"row":427,"column":40},"end":{"row":427,"column":41},"action":"remove","lines":["s"],"id":292},{"start":{"row":427,"column":39},"end":{"row":427,"column":40},"action":"remove","lines":["t"]},{"start":{"row":427,"column":38},"end":{"row":427,"column":39},"action":"remove","lines":["s"]},{"start":{"row":427,"column":37},"end":{"row":427,"column":38},"action":"remove","lines":["e"]},{"start":{"row":427,"column":36},"end":{"row":427,"column":37},"action":"remove","lines":["u"]},{"start":{"row":427,"column":35},"end":{"row":427,"column":36},"action":"remove","lines":["q"]},{"start":{"row":427,"column":34},"end":{"row":427,"column":35},"action":"remove","lines":["e"]},{"start":{"row":427,"column":33},"end":{"row":427,"column":34},"action":"remove","lines":["r"]},{"start":{"row":427,"column":32},"end":{"row":427,"column":33},"action":"remove","lines":[" "]},{"start":{"row":427,"column":31},"end":{"row":427,"column":32},"action":"remove","lines":["e"]},{"start":{"row":427,"column":30},"end":{"row":427,"column":31},"action":"remove","lines":["v"]},{"start":{"row":427,"column":29},"end":{"row":427,"column":30},"action":"remove","lines":["a"]},{"start":{"row":427,"column":28},"end":{"row":427,"column":29},"action":"remove","lines":["e"]},{"start":{"row":427,"column":27},"end":{"row":427,"column":28},"action":"remove","lines":["l"]},{"start":{"row":427,"column":26},"end":{"row":427,"column":27},"action":"remove","lines":[" "]},{"start":{"row":427,"column":25},"end":{"row":427,"column":26},"action":"remove","lines":["l"]},{"start":{"row":427,"column":24},"end":{"row":427,"column":25},"action":"remove","lines":["a"]},{"start":{"row":427,"column":23},"end":{"row":427,"column":24},"action":"remove","lines":["u"]}],[{"start":{"row":427,"column":22},"end":{"row":427,"column":23},"action":"remove","lines":["n"],"id":293},{"start":{"row":427,"column":21},"end":{"row":427,"column":22},"action":"remove","lines":["n"]}],[{"start":{"row":427,"column":21},"end":{"row":427,"column":22},"action":"insert","lines":["v"],"id":294},{"start":{"row":427,"column":22},"end":{"row":427,"column":23},"action":"insert","lines":["a"]},{"start":{"row":427,"column":23},"end":{"row":427,"column":24},"action":"insert","lines":["i"]},{"start":{"row":427,"column":24},"end":{"row":427,"column":25},"action":"insert","lines":["l"]},{"start":{"row":427,"column":25},"end":{"row":427,"column":26},"action":"insert","lines":["a"]},{"start":{"row":427,"column":26},"end":{"row":427,"column":27},"action":"insert","lines":["b"]},{"start":{"row":427,"column":27},"end":{"row":427,"column":28},"action":"insert","lines":["i"]},{"start":{"row":427,"column":28},"end":{"row":427,"column":29},"action":"insert","lines":["l"]}],[{"start":{"row":427,"column":29},"end":{"row":427,"column":30},"action":"insert","lines":["i"],"id":295},{"start":{"row":427,"column":30},"end":{"row":427,"column":31},"action":"insert","lines":["t"]},{"start":{"row":427,"column":31},"end":{"row":427,"column":32},"action":"insert","lines":["y"]}],[{"start":{"row":427,"column":32},"end":{"row":427,"column":33},"action":"insert","lines":[" "],"id":296},{"start":{"row":427,"column":33},"end":{"row":427,"column":34},"action":"insert","lines":["s"]},{"start":{"row":427,"column":34},"end":{"row":427,"column":35},"action":"insert","lines":["h"]},{"start":{"row":427,"column":35},"end":{"row":427,"column":36},"action":"insert","lines":["e"]}],[{"start":{"row":427,"column":35},"end":{"row":427,"column":36},"action":"remove","lines":["e"],"id":297}],[{"start":{"row":427,"column":35},"end":{"row":427,"column":36},"action":"insert","lines":["e"],"id":298},{"start":{"row":427,"column":36},"end":{"row":427,"column":37},"action":"insert","lines":["e"]},{"start":{"row":427,"column":37},"end":{"row":427,"column":38},"action":"insert","lines":["t"]},{"start":{"row":427,"column":38},"end":{"row":427,"column":39},"action":"insert","lines":["s"]},{"start":{"row":427,"column":39},"end":{"row":427,"column":40},"action":"insert","lines":["."]}],[{"start":{"row":428,"column":5},"end":{"row":428,"column":6},"action":"remove","lines":["l"],"id":299}],[{"start":{"row":428,"column":5},"end":{"row":428,"column":6},"action":"insert","lines":["v"],"id":300},{"start":{"row":428,"column":6},"end":{"row":428,"column":7},"action":"insert","lines":["a"]},{"start":{"row":428,"column":7},"end":{"row":428,"column":8},"action":"insert","lines":["i"]},{"start":{"row":428,"column":8},"end":{"row":428,"column":9},"action":"insert","lines":["l"]}],[{"start":{"row":428,"column":9},"end":{"row":428,"column":10},"action":"insert","lines":["_"],"id":301},{"start":{"row":428,"column":10},"end":{"row":428,"column":11},"action":"insert","lines":["h"]},{"start":{"row":428,"column":11},"end":{"row":428,"column":12},"action":"insert","lines":["e"]},{"start":{"row":428,"column":12},"end":{"row":428,"column":13},"action":"insert","lines":["e"]},{"start":{"row":428,"column":13},"end":{"row":428,"column":14},"action":"insert","lines":["t"]}],[{"start":{"row":428,"column":13},"end":{"row":428,"column":14},"action":"remove","lines":["t"],"id":302},{"start":{"row":428,"column":12},"end":{"row":428,"column":13},"action":"remove","lines":["e"]},{"start":{"row":428,"column":11},"end":{"row":428,"column":12},"action":"remove","lines":["e"]},{"start":{"row":428,"column":10},"end":{"row":428,"column":11},"action":"remove","lines":["h"]}],[{"start":{"row":428,"column":10},"end":{"row":428,"column":11},"action":"insert","lines":["s"],"id":303},{"start":{"row":428,"column":11},"end":{"row":428,"column":12},"action":"insert","lines":["h"]},{"start":{"row":428,"column":12},"end":{"row":428,"column":13},"action":"insert","lines":["e"]},{"start":{"row":428,"column":13},"end":{"row":428,"column":14},"action":"insert","lines":["e"]},{"start":{"row":428,"column":14},"end":{"row":428,"column":15},"action":"insert","lines":["t"]}],[{"start":{"row":429,"column":5},"end":{"row":429,"column":6},"action":"remove","lines":["l"],"id":304}],[{"start":{"row":429,"column":5},"end":{"row":429,"column":6},"action":"insert","lines":["v"],"id":305},{"start":{"row":429,"column":6},"end":{"row":429,"column":7},"action":"insert","lines":["a"]},{"start":{"row":429,"column":7},"end":{"row":429,"column":8},"action":"insert","lines":["i"]},{"start":{"row":429,"column":8},"end":{"row":429,"column":9},"action":"insert","lines":["l"]},{"start":{"row":429,"column":9},"end":{"row":429,"column":10},"action":"insert","lines":["_"]},{"start":{"row":429,"column":10},"end":{"row":429,"column":11},"action":"insert","lines":["s"]}],[{"start":{"row":429,"column":11},"end":{"row":429,"column":12},"action":"insert","lines":["h"],"id":306},{"start":{"row":429,"column":12},"end":{"row":429,"column":13},"action":"insert","lines":["e"]},{"start":{"row":429,"column":13},"end":{"row":429,"column":14},"action":"insert","lines":["e"]},{"start":{"row":429,"column":14},"end":{"row":429,"column":15},"action":"insert","lines":["t"]}],[{"start":{"row":429,"column":41},"end":{"row":429,"column":42},"action":"remove","lines":["l"],"id":307}],[{"start":{"row":429,"column":41},"end":{"row":429,"column":42},"action":"insert","lines":["v"],"id":308},{"start":{"row":429,"column":42},"end":{"row":429,"column":43},"action":"insert","lines":["a"]},{"start":{"row":429,"column":43},"end":{"row":429,"column":44},"action":"insert","lines":["i"]},{"start":{"row":429,"column":44},"end":{"row":429,"column":45},"action":"insert","lines":["l"]}],[{"start":{"row":429,"column":40},"end":{"row":429,"column":50},"action":"remove","lines":["avail_page"],"id":309},{"start":{"row":429,"column":40},"end":{"row":429,"column":56},"action":"insert","lines":["avail_sheet_page"]}],[{"start":{"row":429,"column":60},"end":{"row":429,"column":61},"action":"remove","lines":["l"],"id":310}],[{"start":{"row":429,"column":60},"end":{"row":429,"column":61},"action":"insert","lines":["v"],"id":311},{"start":{"row":429,"column":61},"end":{"row":429,"column":62},"action":"insert","lines":["a"]},{"start":{"row":429,"column":62},"end":{"row":429,"column":63},"action":"insert","lines":["i"]},{"start":{"row":429,"column":63},"end":{"row":429,"column":64},"action":"insert","lines":["l"]}],[{"start":{"row":429,"column":64},"end":{"row":429,"column":65},"action":"insert","lines":["_"],"id":312},{"start":{"row":429,"column":65},"end":{"row":429,"column":66},"action":"insert","lines":["s"]},{"start":{"row":429,"column":66},"end":{"row":429,"column":67},"action":"insert","lines":["h"]},{"start":{"row":429,"column":67},"end":{"row":429,"column":68},"action":"insert","lines":["e"]},{"start":{"row":429,"column":68},"end":{"row":429,"column":69},"action":"insert","lines":["e"]},{"start":{"row":429,"column":69},"end":{"row":429,"column":70},"action":"insert","lines":["t"]}],[{"start":{"row":431,"column":5},"end":{"row":431,"column":6},"action":"remove","lines":["l"],"id":313}],[{"start":{"row":431,"column":5},"end":{"row":431,"column":6},"action":"insert","lines":["v"],"id":314},{"start":{"row":431,"column":6},"end":{"row":431,"column":7},"action":"insert","lines":["a"]},{"start":{"row":431,"column":7},"end":{"row":431,"column":8},"action":"insert","lines":["i"]},{"start":{"row":431,"column":8},"end":{"row":431,"column":9},"action":"insert","lines":["l"]},{"start":{"row":431,"column":9},"end":{"row":431,"column":10},"action":"insert","lines":["_"]},{"start":{"row":431,"column":10},"end":{"row":431,"column":11},"action":"insert","lines":["s"]},{"start":{"row":431,"column":11},"end":{"row":431,"column":12},"action":"insert","lines":["h"]},{"start":{"row":431,"column":12},"end":{"row":431,"column":13},"action":"insert","lines":["e"]}],[{"start":{"row":431,"column":13},"end":{"row":431,"column":14},"action":"insert","lines":["e"],"id":315},{"start":{"row":431,"column":14},"end":{"row":431,"column":15},"action":"insert","lines":["t"]}],[{"start":{"row":431,"column":38},"end":{"row":431,"column":62},"action":"remove","lines":["my_annual_leave_requests"],"id":316},{"start":{"row":431,"column":38},"end":{"row":431,"column":60},"action":"insert","lines":["my_availability_sheets"]}],[{"start":{"row":433,"column":16},"end":{"row":433,"column":18},"action":"remove","lines":["al"],"id":317},{"start":{"row":433,"column":16},"end":{"row":433,"column":27},"action":"insert","lines":["avail_sheet"]}],[{"start":{"row":433,"column":43},"end":{"row":433,"column":45},"action":"remove","lines":["al"],"id":318},{"start":{"row":433,"column":43},"end":{"row":433,"column":54},"action":"insert","lines":["avail_sheet"]}],[{"start":{"row":435,"column":16},"end":{"row":435,"column":18},"action":"remove","lines":["al"],"id":319},{"start":{"row":435,"column":16},"end":{"row":435,"column":27},"action":"insert","lines":["avail_sheet"]}],[{"start":{"row":437,"column":16},"end":{"row":437,"column":18},"action":"remove","lines":["al"],"id":320},{"start":{"row":437,"column":16},"end":{"row":437,"column":27},"action":"insert","lines":["avail_sheet"]}],[{"start":{"row":437,"column":43},"end":{"row":437,"column":45},"action":"remove","lines":["al"],"id":321},{"start":{"row":437,"column":43},"end":{"row":437,"column":54},"action":"insert","lines":["avail_sheet"]}],[{"start":{"row":433,"column":12},"end":{"row":433,"column":13},"action":"remove","lines":["l"],"id":322}],[{"start":{"row":433,"column":12},"end":{"row":433,"column":13},"action":"insert","lines":["v"],"id":323},{"start":{"row":433,"column":13},"end":{"row":433,"column":14},"action":"insert","lines":["a"]},{"start":{"row":433,"column":14},"end":{"row":433,"column":15},"action":"insert","lines":["i"]},{"start":{"row":433,"column":15},"end":{"row":433,"column":16},"action":"insert","lines":["l"]},{"start":{"row":433,"column":16},"end":{"row":433,"column":17},"action":"insert","lines":["_"]}],[{"start":{"row":433,"column":17},"end":{"row":433,"column":18},"action":"insert","lines":["s"],"id":324},{"start":{"row":433,"column":18},"end":{"row":433,"column":19},"action":"insert","lines":["h"]},{"start":{"row":433,"column":19},"end":{"row":433,"column":20},"action":"insert","lines":["e"]},{"start":{"row":433,"column":20},"end":{"row":433,"column":21},"action":"insert","lines":["e"]},{"start":{"row":433,"column":21},"end":{"row":433,"column":22},"action":"insert","lines":["t"]},{"start":{"row":433,"column":22},"end":{"row":433,"column":23},"action":"insert","lines":["s"]}],[{"start":{"row":435,"column":11},"end":{"row":435,"column":13},"action":"remove","lines":["al"],"id":325},{"start":{"row":435,"column":11},"end":{"row":435,"column":23},"action":"insert","lines":["avail_sheets"]}],[{"start":{"row":437,"column":11},"end":{"row":437,"column":13},"action":"remove","lines":["al"],"id":326},{"start":{"row":437,"column":11},"end":{"row":437,"column":23},"action":"insert","lines":["avail_sheets"]}],[{"start":{"row":439,"column":55},"end":{"row":439,"column":77},"action":"remove","lines":["my_availability_sheets"],"id":327},{"start":{"row":439,"column":55},"end":{"row":439,"column":70},"action":"insert","lines":["my_avail_sheets"]}],[{"start":{"row":439,"column":73},"end":{"row":439,"column":95},"action":"remove","lines":["my_availability_sheets"],"id":328},{"start":{"row":439,"column":73},"end":{"row":439,"column":88},"action":"insert","lines":["my_avail_sheets"]}],[{"start":{"row":437,"column":85},"end":{"row":438,"column":0},"action":"insert","lines":["",""],"id":329},{"start":{"row":438,"column":0},"end":{"row":438,"column":8},"action":"insert","lines":["        "]},{"start":{"row":438,"column":8},"end":{"row":439,"column":0},"action":"insert","lines":["",""]},{"start":{"row":439,"column":0},"end":{"row":439,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":439,"column":4},"end":{"row":439,"column":8},"action":"remove","lines":["    "],"id":330}],[{"start":{"row":439,"column":4},"end":{"row":449,"column":85},"action":"insert","lines":[" #pagination for availability sheets.","    avail_sheet_page_number = 1","    avail_sheet_page = request.GET.get('avail_sheet_page', avail_sheet_page_number)","    ","    avail_sheet_paginator = Paginator(my_availability_sheets, 2)","    try:","        my_avail_sheets = avail_sheet_paginator.page(avail_sheet_page)","    except PageNotAnInteger:","        my_avail_sheets = avail_sheet_paginator.page(1)","    except EmptyPage:","        my_avail_sheets = avail_sheet_paginator.page(avail_sheet_paginator.num_pages)"],"id":331}],[{"start":{"row":440,"column":14},"end":{"row":440,"column":15},"action":"remove","lines":["t"],"id":332},{"start":{"row":440,"column":13},"end":{"row":440,"column":14},"action":"remove","lines":["e"]},{"start":{"row":440,"column":12},"end":{"row":440,"column":13},"action":"remove","lines":["e"]},{"start":{"row":440,"column":11},"end":{"row":440,"column":12},"action":"remove","lines":["h"]},{"start":{"row":440,"column":10},"end":{"row":440,"column":11},"action":"remove","lines":["s"]},{"start":{"row":440,"column":9},"end":{"row":440,"column":10},"action":"remove","lines":["_"]}],[{"start":{"row":440,"column":4},"end":{"row":440,"column":5},"action":"insert","lines":["s"],"id":333},{"start":{"row":440,"column":5},"end":{"row":440,"column":6},"action":"insert","lines":["t"]},{"start":{"row":440,"column":6},"end":{"row":440,"column":7},"action":"insert","lines":["_"]}],[{"start":{"row":441,"column":4},"end":{"row":441,"column":5},"action":"insert","lines":["s"],"id":334},{"start":{"row":441,"column":5},"end":{"row":441,"column":6},"action":"insert","lines":["t"]},{"start":{"row":441,"column":6},"end":{"row":441,"column":7},"action":"insert","lines":["_"]}],[{"start":{"row":441,"column":17},"end":{"row":441,"column":18},"action":"remove","lines":["t"],"id":335},{"start":{"row":441,"column":16},"end":{"row":441,"column":17},"action":"remove","lines":["e"]},{"start":{"row":441,"column":15},"end":{"row":441,"column":16},"action":"remove","lines":["e"]},{"start":{"row":441,"column":14},"end":{"row":441,"column":15},"action":"remove","lines":["h"]},{"start":{"row":441,"column":13},"end":{"row":441,"column":14},"action":"remove","lines":["s"]},{"start":{"row":441,"column":12},"end":{"row":441,"column":13},"action":"remove","lines":["_"]}],[{"start":{"row":441,"column":47},"end":{"row":441,"column":48},"action":"remove","lines":["t"],"id":336},{"start":{"row":441,"column":46},"end":{"row":441,"column":47},"action":"remove","lines":["e"]},{"start":{"row":441,"column":45},"end":{"row":441,"column":46},"action":"remove","lines":["e"]},{"start":{"row":441,"column":44},"end":{"row":441,"column":45},"action":"remove","lines":["h"]},{"start":{"row":441,"column":43},"end":{"row":441,"column":44},"action":"remove","lines":["s"]},{"start":{"row":441,"column":42},"end":{"row":441,"column":43},"action":"remove","lines":["_"]}],[{"start":{"row":441,"column":37},"end":{"row":441,"column":38},"action":"insert","lines":["s"],"id":337},{"start":{"row":441,"column":38},"end":{"row":441,"column":39},"action":"insert","lines":["t"]},{"start":{"row":441,"column":39},"end":{"row":441,"column":40},"action":"insert","lines":["_"]}],[{"start":{"row":441,"column":53},"end":{"row":441,"column":54},"action":"insert","lines":["s"],"id":338},{"start":{"row":441,"column":54},"end":{"row":441,"column":55},"action":"insert","lines":["t"]},{"start":{"row":441,"column":55},"end":{"row":441,"column":56},"action":"insert","lines":["+"]}],[{"start":{"row":441,"column":55},"end":{"row":441,"column":56},"action":"remove","lines":["+"],"id":339}],[{"start":{"row":441,"column":55},"end":{"row":441,"column":56},"action":"insert","lines":["_"],"id":340}],[{"start":{"row":441,"column":67},"end":{"row":441,"column":68},"action":"remove","lines":["_"],"id":341},{"start":{"row":441,"column":66},"end":{"row":441,"column":67},"action":"remove","lines":["t"]},{"start":{"row":441,"column":65},"end":{"row":441,"column":66},"action":"remove","lines":["e"]},{"start":{"row":441,"column":64},"end":{"row":441,"column":65},"action":"remove","lines":["e"]},{"start":{"row":441,"column":63},"end":{"row":441,"column":64},"action":"remove","lines":["h"]},{"start":{"row":441,"column":62},"end":{"row":441,"column":63},"action":"remove","lines":["s"]},{"start":{"row":441,"column":61},"end":{"row":441,"column":62},"action":"remove","lines":["_"]}],[{"start":{"row":441,"column":61},"end":{"row":441,"column":62},"action":"insert","lines":["_"],"id":342}],[{"start":{"row":443,"column":14},"end":{"row":443,"column":15},"action":"remove","lines":["t"],"id":343},{"start":{"row":443,"column":13},"end":{"row":443,"column":14},"action":"remove","lines":["e"]},{"start":{"row":443,"column":12},"end":{"row":443,"column":13},"action":"remove","lines":["e"]},{"start":{"row":443,"column":11},"end":{"row":443,"column":12},"action":"remove","lines":["h"]},{"start":{"row":443,"column":10},"end":{"row":443,"column":11},"action":"remove","lines":["s"]},{"start":{"row":443,"column":9},"end":{"row":443,"column":10},"action":"remove","lines":["_"]},{"start":{"row":443,"column":8},"end":{"row":443,"column":9},"action":"remove","lines":["l"]}],[{"start":{"row":443,"column":8},"end":{"row":443,"column":9},"action":"insert","lines":["l"],"id":344}],[{"start":{"row":443,"column":4},"end":{"row":443,"column":5},"action":"insert","lines":["s"],"id":345},{"start":{"row":443,"column":5},"end":{"row":443,"column":6},"action":"insert","lines":["t"]},{"start":{"row":443,"column":6},"end":{"row":443,"column":7},"action":"insert","lines":["_"]}],[{"start":{"row":443,"column":35},"end":{"row":443,"column":57},"action":"remove","lines":["my_availability_sheets"],"id":346},{"start":{"row":443,"column":35},"end":{"row":443,"column":61},"action":"insert","lines":["my_short_term_availability"]}],[{"start":{"row":445,"column":26},"end":{"row":445,"column":47},"action":"remove","lines":["avail_sheet_paginator"],"id":347},{"start":{"row":445,"column":26},"end":{"row":445,"column":44},"action":"insert","lines":["st_avail_paginator"]}],[{"start":{"row":447,"column":26},"end":{"row":447,"column":47},"action":"remove","lines":["avail_sheet_paginator"],"id":348},{"start":{"row":447,"column":26},"end":{"row":447,"column":44},"action":"insert","lines":["st_avail_paginator"]}],[{"start":{"row":449,"column":26},"end":{"row":449,"column":47},"action":"remove","lines":["avail_sheet_paginator"],"id":349},{"start":{"row":449,"column":26},"end":{"row":449,"column":44},"action":"insert","lines":["st_avail_paginator"]}],[{"start":{"row":449,"column":50},"end":{"row":449,"column":71},"action":"remove","lines":["avail_sheet_paginator"],"id":350},{"start":{"row":449,"column":50},"end":{"row":449,"column":68},"action":"insert","lines":["st_avail_paginator"]}],[{"start":{"row":445,"column":50},"end":{"row":445,"column":66},"action":"remove","lines":["avail_sheet_page"],"id":351},{"start":{"row":445,"column":50},"end":{"row":445,"column":63},"action":"insert","lines":["st_avail_page"]}],[{"start":{"row":445,"column":11},"end":{"row":445,"column":12},"action":"insert","lines":["s"],"id":352},{"start":{"row":445,"column":12},"end":{"row":445,"column":13},"action":"insert","lines":["t"]},{"start":{"row":445,"column":13},"end":{"row":445,"column":14},"action":"insert","lines":["_"]}],[{"start":{"row":445,"column":25},"end":{"row":445,"column":26},"action":"remove","lines":["s"],"id":353},{"start":{"row":445,"column":24},"end":{"row":445,"column":25},"action":"remove","lines":["t"]},{"start":{"row":445,"column":23},"end":{"row":445,"column":24},"action":"remove","lines":["e"]},{"start":{"row":445,"column":22},"end":{"row":445,"column":23},"action":"remove","lines":["e"]},{"start":{"row":445,"column":21},"end":{"row":445,"column":22},"action":"remove","lines":["h"]},{"start":{"row":445,"column":20},"end":{"row":445,"column":21},"action":"remove","lines":["s"]},{"start":{"row":445,"column":19},"end":{"row":445,"column":20},"action":"remove","lines":["_"]}],[{"start":{"row":447,"column":8},"end":{"row":447,"column":23},"action":"remove","lines":["my_avail_sheets"],"id":354},{"start":{"row":447,"column":8},"end":{"row":447,"column":19},"action":"insert","lines":["my_st_avail"]}],[{"start":{"row":447,"column":19},"end":{"row":447,"column":20},"action":"insert","lines":["s"],"id":355}],[{"start":{"row":445,"column":19},"end":{"row":445,"column":20},"action":"insert","lines":["s"],"id":356}],[{"start":{"row":449,"column":7},"end":{"row":449,"column":23},"action":"remove","lines":[" my_avail_sheets"],"id":357},{"start":{"row":449,"column":7},"end":{"row":449,"column":18},"action":"insert","lines":["my_st_avail"]}],[{"start":{"row":449,"column":7},"end":{"row":449,"column":8},"action":"insert","lines":[" "],"id":358}],[{"start":{"row":449,"column":19},"end":{"row":449,"column":20},"action":"insert","lines":["s"],"id":359}],[{"start":{"row":451,"column":91},"end":{"row":451,"column":117},"action":"remove","lines":["my_short_term_availability"],"id":360},{"start":{"row":451,"column":91},"end":{"row":451,"column":103},"action":"insert","lines":["my_st_avails"]}],[{"start":{"row":451,"column":106},"end":{"row":451,"column":132},"action":"remove","lines":["my_short_term_availability"],"id":361},{"start":{"row":451,"column":106},"end":{"row":451,"column":118},"action":"insert","lines":["my_st_avails"]}]]},"ace":{"folds":[],"scrolltop":5861,"scrollleft":0,"selection":{"start":{"row":441,"column":4},"end":{"row":441,"column":17},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":417,"state":"start","mode":"ace/mode/python"}},"timestamp":1615738076061,"hash":"46ed8e26951e3cb3c3cee96771070d7e0d9b477e"}