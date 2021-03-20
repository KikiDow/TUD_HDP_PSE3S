{"filter":false,"title":"views.py","tooltip":"/exchanges/views.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":80,"column":18},"end":{"row":80,"column":21},"action":"remove","lines":["csl"],"id":28},{"start":{"row":80,"column":18},"end":{"row":80,"column":43},"action":"insert","lines":["exchanges_req_started_pag"]}],[{"start":{"row":80,"column":59},"end":{"row":80,"column":62},"action":"remove","lines":["csl"],"id":29},{"start":{"row":80,"column":59},"end":{"row":80,"column":84},"action":"insert","lines":["exchanges_req_started_pag"]}],[{"start":{"row":76,"column":11},"end":{"row":76,"column":15},"action":"remove","lines":["csls"],"id":30},{"start":{"row":76,"column":11},"end":{"row":76,"column":32},"action":"insert","lines":["exchanges_req_started"]}],[{"start":{"row":78,"column":11},"end":{"row":78,"column":15},"action":"remove","lines":["csls"],"id":31},{"start":{"row":78,"column":11},"end":{"row":78,"column":32},"action":"insert","lines":["exchanges_req_started"]}],[{"start":{"row":80,"column":11},"end":{"row":80,"column":15},"action":"remove","lines":["csls"],"id":32},{"start":{"row":80,"column":11},"end":{"row":80,"column":32},"action":"insert","lines":["exchanges_req_started"]}],[{"start":{"row":82,"column":56},"end":{"row":82,"column":77},"action":"remove","lines":["exchanges_req_started"],"id":33},{"start":{"row":82,"column":56},"end":{"row":82,"column":80},"action":"insert","lines":["my_exchanges_req_started"]}],[{"start":{"row":82,"column":83},"end":{"row":82,"column":104},"action":"remove","lines":["exchanges_req_started"],"id":34},{"start":{"row":82,"column":83},"end":{"row":82,"column":107},"action":"insert","lines":["my_exchanges_req_started"]}],[{"start":{"row":80,"column":122},"end":{"row":81,"column":0},"action":"insert","lines":["",""],"id":35},{"start":{"row":81,"column":0},"end":{"row":81,"column":8},"action":"insert","lines":["        "]},{"start":{"row":81,"column":8},"end":{"row":82,"column":0},"action":"insert","lines":["",""]},{"start":{"row":82,"column":0},"end":{"row":82,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":82,"column":4},"end":{"row":82,"column":8},"action":"remove","lines":["    "],"id":36}],[{"start":{"row":82,"column":4},"end":{"row":92,"column":61},"action":"insert","lines":["#Pagination for CSLs","    csl_page_number = 1","    csl_page = request.GET.get('csl_page', csl_page_number)","    ","    csl_paginator = Paginator(my_csl, 3)","    try:","        my_csls = csl_paginator.page(csl_page)","    except PageNotAnInteger:","        my_csls = csl_paginator.page(1)","    except EmptyPage:","        my_csls = csl_paginator.page(csl_paginator.num_pages)"],"id":37}],[{"start":{"row":82,"column":22},"end":{"row":82,"column":23},"action":"remove","lines":["L"],"id":38},{"start":{"row":82,"column":21},"end":{"row":82,"column":22},"action":"remove","lines":["S"]},{"start":{"row":82,"column":20},"end":{"row":82,"column":21},"action":"remove","lines":["C"]}],[{"start":{"row":82,"column":20},"end":{"row":82,"column":21},"action":"insert","lines":["R"],"id":39},{"start":{"row":82,"column":21},"end":{"row":82,"column":22},"action":"insert","lines":["e"]},{"start":{"row":82,"column":22},"end":{"row":82,"column":23},"action":"insert","lines":["q"]},{"start":{"row":82,"column":23},"end":{"row":82,"column":24},"action":"insert","lines":["u"]},{"start":{"row":82,"column":24},"end":{"row":82,"column":25},"action":"insert","lines":["e"]},{"start":{"row":82,"column":25},"end":{"row":82,"column":26},"action":"insert","lines":["s"]},{"start":{"row":82,"column":26},"end":{"row":82,"column":27},"action":"insert","lines":["t"]}],[{"start":{"row":82,"column":27},"end":{"row":82,"column":28},"action":"insert","lines":["s"],"id":40}],[{"start":{"row":82,"column":27},"end":{"row":82,"column":28},"action":"remove","lines":["s"],"id":41}],[{"start":{"row":82,"column":28},"end":{"row":82,"column":29},"action":"insert","lines":[" "],"id":42},{"start":{"row":82,"column":29},"end":{"row":82,"column":30},"action":"insert","lines":["a"]},{"start":{"row":82,"column":30},"end":{"row":82,"column":31},"action":"insert","lines":["w"]},{"start":{"row":82,"column":31},"end":{"row":82,"column":32},"action":"insert","lines":["a"]},{"start":{"row":82,"column":32},"end":{"row":82,"column":33},"action":"insert","lines":["i"]},{"start":{"row":82,"column":33},"end":{"row":82,"column":34},"action":"insert","lines":["t"]}],[{"start":{"row":82,"column":34},"end":{"row":82,"column":35},"action":"insert","lines":["i"],"id":43},{"start":{"row":82,"column":35},"end":{"row":82,"column":36},"action":"insert","lines":["n"]},{"start":{"row":82,"column":36},"end":{"row":82,"column":37},"action":"insert","lines":["g"]}],[{"start":{"row":82,"column":36},"end":{"row":82,"column":37},"action":"remove","lines":["g"],"id":44},{"start":{"row":82,"column":35},"end":{"row":82,"column":36},"action":"remove","lines":["n"]},{"start":{"row":82,"column":34},"end":{"row":82,"column":35},"action":"remove","lines":["i"]},{"start":{"row":82,"column":33},"end":{"row":82,"column":34},"action":"remove","lines":["t"]},{"start":{"row":82,"column":32},"end":{"row":82,"column":33},"action":"remove","lines":["i"]},{"start":{"row":82,"column":31},"end":{"row":82,"column":32},"action":"remove","lines":["a"]},{"start":{"row":82,"column":30},"end":{"row":82,"column":31},"action":"remove","lines":["w"]},{"start":{"row":82,"column":29},"end":{"row":82,"column":30},"action":"remove","lines":["a"]}],[{"start":{"row":82,"column":29},"end":{"row":82,"column":30},"action":"insert","lines":["s"],"id":45},{"start":{"row":82,"column":30},"end":{"row":82,"column":31},"action":"insert","lines":["t"]},{"start":{"row":82,"column":31},"end":{"row":82,"column":32},"action":"insert","lines":["a"]},{"start":{"row":82,"column":32},"end":{"row":82,"column":33},"action":"insert","lines":["r"]},{"start":{"row":82,"column":33},"end":{"row":82,"column":34},"action":"insert","lines":["t"]},{"start":{"row":82,"column":34},"end":{"row":82,"column":35},"action":"insert","lines":["d"]}],[{"start":{"row":82,"column":34},"end":{"row":82,"column":35},"action":"remove","lines":["d"],"id":46}],[{"start":{"row":82,"column":34},"end":{"row":82,"column":35},"action":"insert","lines":["e"],"id":47},{"start":{"row":82,"column":35},"end":{"row":82,"column":36},"action":"insert","lines":["d"]}],[{"start":{"row":82,"column":36},"end":{"row":82,"column":37},"action":"insert","lines":[" "],"id":48},{"start":{"row":82,"column":37},"end":{"row":82,"column":38},"action":"insert","lines":["a"]},{"start":{"row":82,"column":38},"end":{"row":82,"column":39},"action":"insert","lines":["w"]},{"start":{"row":82,"column":39},"end":{"row":82,"column":40},"action":"insert","lines":["a"]},{"start":{"row":82,"column":40},"end":{"row":82,"column":41},"action":"insert","lines":["i"]},{"start":{"row":82,"column":41},"end":{"row":82,"column":42},"action":"insert","lines":["t"]},{"start":{"row":82,"column":42},"end":{"row":82,"column":43},"action":"insert","lines":["i"]},{"start":{"row":82,"column":43},"end":{"row":82,"column":44},"action":"insert","lines":["n"]},{"start":{"row":82,"column":44},"end":{"row":82,"column":45},"action":"insert","lines":["g"]}],[{"start":{"row":82,"column":45},"end":{"row":82,"column":46},"action":"insert","lines":[" "],"id":49},{"start":{"row":82,"column":46},"end":{"row":82,"column":47},"action":"insert","lines":["r"]},{"start":{"row":82,"column":47},"end":{"row":82,"column":48},"action":"insert","lines":["e"]},{"start":{"row":82,"column":48},"end":{"row":82,"column":49},"action":"insert","lines":["p"]},{"start":{"row":82,"column":49},"end":{"row":82,"column":50},"action":"insert","lines":["l"]},{"start":{"row":82,"column":50},"end":{"row":82,"column":51},"action":"insert","lines":["y"]}],[{"start":{"row":82,"column":51},"end":{"row":82,"column":52},"action":"insert","lines":["."],"id":50}],[{"start":{"row":83,"column":4},"end":{"row":83,"column":7},"action":"remove","lines":["csl"],"id":51},{"start":{"row":83,"column":4},"end":{"row":83,"column":32},"action":"insert","lines":["exchanges_req_awaiting_reply"]}],[{"start":{"row":84,"column":4},"end":{"row":84,"column":7},"action":"remove","lines":["csl"],"id":52},{"start":{"row":84,"column":4},"end":{"row":84,"column":32},"action":"insert","lines":["exchanges_req_awaiting_reply"]}],[{"start":{"row":84,"column":57},"end":{"row":84,"column":60},"action":"remove","lines":["csl"],"id":53},{"start":{"row":84,"column":57},"end":{"row":84,"column":85},"action":"insert","lines":["exchanges_req_awaiting_reply"]}],[{"start":{"row":84,"column":93},"end":{"row":84,"column":96},"action":"remove","lines":["csl"],"id":54},{"start":{"row":84,"column":93},"end":{"row":84,"column":121},"action":"insert","lines":["exchanges_req_awaiting_reply"]}],[{"start":{"row":86,"column":4},"end":{"row":86,"column":7},"action":"remove","lines":["csl"],"id":55},{"start":{"row":86,"column":4},"end":{"row":86,"column":32},"action":"insert","lines":["exchanges_req_awaiting_reply"]}],[{"start":{"row":86,"column":55},"end":{"row":86,"column":61},"action":"remove","lines":["my_csl"],"id":56},{"start":{"row":86,"column":55},"end":{"row":86,"column":83},"action":"insert","lines":["exchanges_req_awaiting_reply"]}],[{"start":{"row":88,"column":18},"end":{"row":88,"column":21},"action":"remove","lines":["csl"],"id":57},{"start":{"row":88,"column":18},"end":{"row":88,"column":46},"action":"insert","lines":["exchanges_req_awaiting_reply"]}],[{"start":{"row":88,"column":62},"end":{"row":88,"column":65},"action":"remove","lines":["csl"],"id":58},{"start":{"row":88,"column":62},"end":{"row":88,"column":90},"action":"insert","lines":["exchanges_req_awaiting_reply"]}],[{"start":{"row":90,"column":18},"end":{"row":90,"column":21},"action":"remove","lines":["csl"],"id":59},{"start":{"row":90,"column":18},"end":{"row":90,"column":46},"action":"insert","lines":["exchanges_req_awaiting_reply"]}],[{"start":{"row":92,"column":18},"end":{"row":92,"column":21},"action":"remove","lines":["csl"],"id":60},{"start":{"row":92,"column":18},"end":{"row":92,"column":46},"action":"insert","lines":["exchanges_req_awaiting_reply"]}],[{"start":{"row":92,"column":62},"end":{"row":92,"column":65},"action":"remove","lines":["csl"],"id":61},{"start":{"row":92,"column":62},"end":{"row":92,"column":90},"action":"insert","lines":["exchanges_req_awaiting_reply"]}],[{"start":{"row":88,"column":11},"end":{"row":88,"column":15},"action":"remove","lines":["csls"],"id":62},{"start":{"row":88,"column":11},"end":{"row":88,"column":39},"action":"insert","lines":["exchanges_req_awaiting_reply"]}],[{"start":{"row":90,"column":11},"end":{"row":90,"column":15},"action":"remove","lines":["csls"],"id":63},{"start":{"row":90,"column":11},"end":{"row":90,"column":39},"action":"insert","lines":["exchanges_req_awaiting_reply"]}],[{"start":{"row":92,"column":11},"end":{"row":92,"column":15},"action":"remove","lines":["csls"],"id":64},{"start":{"row":92,"column":11},"end":{"row":92,"column":39},"action":"insert","lines":["exchanges_req_awaiting_reply"]}],[{"start":{"row":94,"column":110},"end":{"row":94,"column":138},"action":"remove","lines":["exchanges_req_awaiting_reply"],"id":65},{"start":{"row":94,"column":110},"end":{"row":94,"column":141},"action":"insert","lines":["my_exchanges_req_awaiting_reply"]}],[{"start":{"row":94,"column":144},"end":{"row":94,"column":172},"action":"remove","lines":["exchanges_req_awaiting_reply"],"id":66},{"start":{"row":94,"column":144},"end":{"row":94,"column":175},"action":"insert","lines":["my_exchanges_req_awaiting_reply"]}],[{"start":{"row":92,"column":135},"end":{"row":93,"column":0},"action":"insert","lines":["",""],"id":67},{"start":{"row":93,"column":0},"end":{"row":93,"column":8},"action":"insert","lines":["        "]},{"start":{"row":93,"column":8},"end":{"row":94,"column":0},"action":"insert","lines":["",""]},{"start":{"row":94,"column":0},"end":{"row":94,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":94,"column":4},"end":{"row":94,"column":8},"action":"remove","lines":["    "],"id":68}],[{"start":{"row":94,"column":4},"end":{"row":104,"column":61},"action":"insert","lines":["#Pagination for CSLs","    csl_page_number = 1","    csl_page = request.GET.get('csl_page', csl_page_number)","    ","    csl_paginator = Paginator(my_csl, 3)","    try:","        my_csls = csl_paginator.page(csl_page)","    except PageNotAnInteger:","        my_csls = csl_paginator.page(1)","    except EmptyPage:","        my_csls = csl_paginator.page(csl_paginator.num_pages)"],"id":69}],[{"start":{"row":94,"column":23},"end":{"row":94,"column":24},"action":"remove","lines":["s"],"id":70},{"start":{"row":94,"column":22},"end":{"row":94,"column":23},"action":"remove","lines":["L"]},{"start":{"row":94,"column":21},"end":{"row":94,"column":22},"action":"remove","lines":["S"]},{"start":{"row":94,"column":20},"end":{"row":94,"column":21},"action":"remove","lines":["C"]}],[{"start":{"row":94,"column":20},"end":{"row":94,"column":21},"action":"insert","lines":["E"],"id":71},{"start":{"row":94,"column":21},"end":{"row":94,"column":22},"action":"insert","lines":["x"]},{"start":{"row":94,"column":22},"end":{"row":94,"column":23},"action":"insert","lines":["c"]},{"start":{"row":94,"column":23},"end":{"row":94,"column":24},"action":"insert","lines":["h"]},{"start":{"row":94,"column":24},"end":{"row":94,"column":25},"action":"insert","lines":["a"]},{"start":{"row":94,"column":25},"end":{"row":94,"column":26},"action":"insert","lines":["n"]},{"start":{"row":94,"column":26},"end":{"row":94,"column":27},"action":"insert","lines":["g"]},{"start":{"row":94,"column":27},"end":{"row":94,"column":28},"action":"insert","lines":["e"]},{"start":{"row":94,"column":28},"end":{"row":94,"column":29},"action":"insert","lines":["s"]}],[{"start":{"row":94,"column":29},"end":{"row":94,"column":30},"action":"insert","lines":[" "],"id":72}],[{"start":{"row":94,"column":30},"end":{"row":94,"column":72},"action":"insert","lines":["Awaiting Exchanging Officers Confirmation."],"id":73}],[{"start":{"row":94,"column":30},"end":{"row":94,"column":31},"action":"remove","lines":["A"],"id":74}],[{"start":{"row":94,"column":30},"end":{"row":94,"column":31},"action":"insert","lines":["a"],"id":75}],[{"start":{"row":98,"column":30},"end":{"row":98,"column":36},"action":"remove","lines":["my_csl"],"id":76},{"start":{"row":98,"column":30},"end":{"row":98,"column":63},"action":"insert","lines":["exchange_reqs_awaiting_eo_confirm"]}],[{"start":{"row":95,"column":4},"end":{"row":95,"column":7},"action":"remove","lines":["csl"],"id":77},{"start":{"row":95,"column":4},"end":{"row":95,"column":37},"action":"insert","lines":["exchange_reqs_awaiting_eo_confirm"]}],[{"start":{"row":96,"column":4},"end":{"row":96,"column":7},"action":"remove","lines":["csl"],"id":78},{"start":{"row":96,"column":4},"end":{"row":96,"column":37},"action":"insert","lines":["exchange_reqs_awaiting_eo_confirm"]}],[{"start":{"row":96,"column":62},"end":{"row":96,"column":65},"action":"remove","lines":["csl"],"id":79},{"start":{"row":96,"column":62},"end":{"row":96,"column":95},"action":"insert","lines":["exchange_reqs_awaiting_eo_confirm"]}],[{"start":{"row":96,"column":103},"end":{"row":96,"column":106},"action":"remove","lines":["csl"],"id":80},{"start":{"row":96,"column":103},"end":{"row":96,"column":136},"action":"insert","lines":["exchange_reqs_awaiting_eo_confirm"]}],[{"start":{"row":98,"column":4},"end":{"row":98,"column":7},"action":"remove","lines":["csl"],"id":81},{"start":{"row":98,"column":4},"end":{"row":98,"column":37},"action":"insert","lines":["exchange_reqs_awaiting_eo_confirm"]}],[{"start":{"row":100,"column":18},"end":{"row":100,"column":21},"action":"remove","lines":["csl"],"id":82},{"start":{"row":100,"column":18},"end":{"row":100,"column":51},"action":"insert","lines":["exchange_reqs_awaiting_eo_confirm"]}],[{"start":{"row":100,"column":67},"end":{"row":100,"column":70},"action":"remove","lines":["csl"],"id":83},{"start":{"row":100,"column":67},"end":{"row":100,"column":100},"action":"insert","lines":["exchange_reqs_awaiting_eo_confirm"]}],[{"start":{"row":102,"column":18},"end":{"row":102,"column":21},"action":"remove","lines":["csl"],"id":84},{"start":{"row":102,"column":18},"end":{"row":102,"column":51},"action":"insert","lines":["exchange_reqs_awaiting_eo_confirm"]}],[{"start":{"row":104,"column":18},"end":{"row":104,"column":21},"action":"remove","lines":["csl"],"id":85},{"start":{"row":104,"column":18},"end":{"row":104,"column":51},"action":"insert","lines":["exchange_reqs_awaiting_eo_confirm"]}],[{"start":{"row":104,"column":67},"end":{"row":104,"column":70},"action":"remove","lines":["csl"],"id":86},{"start":{"row":104,"column":67},"end":{"row":104,"column":100},"action":"insert","lines":["exchange_reqs_awaiting_eo_confirm"]}],[{"start":{"row":100,"column":11},"end":{"row":100,"column":15},"action":"remove","lines":["csls"],"id":87},{"start":{"row":100,"column":11},"end":{"row":100,"column":44},"action":"insert","lines":["exchange_reqs_awaiting_eo_confirm"]}],[{"start":{"row":102,"column":11},"end":{"row":102,"column":15},"action":"remove","lines":["csls"],"id":88},{"start":{"row":102,"column":11},"end":{"row":102,"column":44},"action":"insert","lines":["exchange_reqs_awaiting_eo_confirm"]}],[{"start":{"row":104,"column":11},"end":{"row":104,"column":15},"action":"remove","lines":["csls"],"id":89},{"start":{"row":104,"column":11},"end":{"row":104,"column":44},"action":"insert","lines":["exchange_reqs_awaiting_eo_confirm"]}],[{"start":{"row":106,"column":178},"end":{"row":106,"column":211},"action":"remove","lines":["exchange_reqs_awaiting_eo_confirm"],"id":90},{"start":{"row":106,"column":178},"end":{"row":106,"column":214},"action":"insert","lines":["my_exchange_reqs_awaiting_eo_confirm"]}],[{"start":{"row":106,"column":217},"end":{"row":106,"column":250},"action":"remove","lines":["exchange_reqs_awaiting_eo_confirm"],"id":91},{"start":{"row":106,"column":217},"end":{"row":106,"column":253},"action":"insert","lines":["my_exchange_reqs_awaiting_eo_confirm"]}],[{"start":{"row":104,"column":150},"end":{"row":105,"column":0},"action":"insert","lines":["",""],"id":92},{"start":{"row":105,"column":0},"end":{"row":105,"column":8},"action":"insert","lines":["        "]},{"start":{"row":105,"column":8},"end":{"row":106,"column":0},"action":"insert","lines":["",""]},{"start":{"row":106,"column":0},"end":{"row":106,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":106,"column":4},"end":{"row":106,"column":8},"action":"remove","lines":["    "],"id":93}],[{"start":{"row":106,"column":4},"end":{"row":116,"column":61},"action":"insert","lines":["#Pagination for CSLs","    csl_page_number = 1","    csl_page = request.GET.get('csl_page', csl_page_number)","    ","    csl_paginator = Paginator(my_csl, 3)","    try:","        my_csls = csl_paginator.page(csl_page)","    except PageNotAnInteger:","        my_csls = csl_paginator.page(1)","    except EmptyPage:","        my_csls = csl_paginator.page(csl_paginator.num_pages)"],"id":94}],[{"start":{"row":106,"column":23},"end":{"row":106,"column":24},"action":"remove","lines":["s"],"id":95},{"start":{"row":106,"column":22},"end":{"row":106,"column":23},"action":"remove","lines":["L"]},{"start":{"row":106,"column":21},"end":{"row":106,"column":22},"action":"remove","lines":["S"]},{"start":{"row":106,"column":20},"end":{"row":106,"column":21},"action":"remove","lines":["C"]}],[{"start":{"row":106,"column":20},"end":{"row":106,"column":21},"action":"insert","lines":["E"],"id":96},{"start":{"row":106,"column":21},"end":{"row":106,"column":22},"action":"insert","lines":["x"]},{"start":{"row":106,"column":22},"end":{"row":106,"column":23},"action":"insert","lines":["c"]},{"start":{"row":106,"column":23},"end":{"row":106,"column":24},"action":"insert","lines":["h"]},{"start":{"row":106,"column":24},"end":{"row":106,"column":25},"action":"insert","lines":["a"]},{"start":{"row":106,"column":25},"end":{"row":106,"column":26},"action":"insert","lines":["n"]},{"start":{"row":106,"column":26},"end":{"row":106,"column":27},"action":"insert","lines":["g"]},{"start":{"row":106,"column":27},"end":{"row":106,"column":28},"action":"insert","lines":["e"]}],[{"start":{"row":106,"column":28},"end":{"row":106,"column":29},"action":"insert","lines":["s"],"id":97}],[{"start":{"row":106,"column":29},"end":{"row":106,"column":30},"action":"insert","lines":[" "],"id":98}],[{"start":{"row":106,"column":30},"end":{"row":106,"column":54},"action":"insert","lines":["Awaiting my confirmation"],"id":99}],[{"start":{"row":106,"column":30},"end":{"row":106,"column":31},"action":"remove","lines":["A"],"id":100}],[{"start":{"row":106,"column":30},"end":{"row":106,"column":31},"action":"insert","lines":["a"],"id":101}],[{"start":{"row":110,"column":30},"end":{"row":110,"column":36},"action":"remove","lines":["my_csl"],"id":102},{"start":{"row":110,"column":30},"end":{"row":110,"column":65},"action":"insert","lines":["exchanges_req_awaiting_confirmation"]}],[{"start":{"row":107,"column":4},"end":{"row":107,"column":7},"action":"remove","lines":["csl"],"id":103},{"start":{"row":107,"column":4},"end":{"row":107,"column":39},"action":"insert","lines":["exchanges_req_awaiting_confirmation"]}],[{"start":{"row":108,"column":4},"end":{"row":108,"column":7},"action":"remove","lines":["csl"],"id":104},{"start":{"row":108,"column":4},"end":{"row":108,"column":39},"action":"insert","lines":["exchanges_req_awaiting_confirmation"]}],[{"start":{"row":108,"column":64},"end":{"row":108,"column":67},"action":"remove","lines":["csl"],"id":105},{"start":{"row":108,"column":64},"end":{"row":108,"column":99},"action":"insert","lines":["exchanges_req_awaiting_confirmation"]}],[{"start":{"row":108,"column":107},"end":{"row":108,"column":110},"action":"remove","lines":["csl"],"id":106},{"start":{"row":108,"column":107},"end":{"row":108,"column":142},"action":"insert","lines":["exchanges_req_awaiting_confirmation"]}],[{"start":{"row":110,"column":4},"end":{"row":110,"column":7},"action":"remove","lines":["csl"],"id":107},{"start":{"row":110,"column":4},"end":{"row":110,"column":39},"action":"insert","lines":["exchanges_req_awaiting_confirmation"]}],[{"start":{"row":112,"column":18},"end":{"row":112,"column":21},"action":"remove","lines":["csl"],"id":108},{"start":{"row":112,"column":18},"end":{"row":112,"column":53},"action":"insert","lines":["exchanges_req_awaiting_confirmation"]}],[{"start":{"row":112,"column":69},"end":{"row":112,"column":72},"action":"remove","lines":["csl"],"id":109},{"start":{"row":112,"column":69},"end":{"row":112,"column":104},"action":"insert","lines":["exchanges_req_awaiting_confirmation"]}],[{"start":{"row":114,"column":18},"end":{"row":114,"column":21},"action":"remove","lines":["csl"],"id":110},{"start":{"row":114,"column":18},"end":{"row":114,"column":53},"action":"insert","lines":["exchanges_req_awaiting_confirmation"]}],[{"start":{"row":116,"column":18},"end":{"row":116,"column":21},"action":"remove","lines":["csl"],"id":111},{"start":{"row":116,"column":18},"end":{"row":116,"column":53},"action":"insert","lines":["exchanges_req_awaiting_confirmation"]}],[{"start":{"row":116,"column":69},"end":{"row":116,"column":72},"action":"remove","lines":["csl"],"id":112},{"start":{"row":116,"column":69},"end":{"row":116,"column":104},"action":"insert","lines":["exchanges_req_awaiting_confirmation"]}],[{"start":{"row":112,"column":11},"end":{"row":112,"column":15},"action":"remove","lines":["csls"],"id":113},{"start":{"row":112,"column":11},"end":{"row":112,"column":46},"action":"insert","lines":["exchanges_req_awaiting_confirmation"]}],[{"start":{"row":114,"column":11},"end":{"row":114,"column":15},"action":"remove","lines":["csls"],"id":114},{"start":{"row":114,"column":11},"end":{"row":114,"column":46},"action":"insert","lines":["exchanges_req_awaiting_confirmation"]}],[{"start":{"row":116,"column":11},"end":{"row":116,"column":15},"action":"remove","lines":["csls"],"id":115},{"start":{"row":116,"column":11},"end":{"row":116,"column":46},"action":"insert","lines":["exchanges_req_awaiting_confirmation"]}],[{"start":{"row":118,"column":256},"end":{"row":118,"column":291},"action":"remove","lines":["exchanges_req_awaiting_confirmation"],"id":116},{"start":{"row":118,"column":256},"end":{"row":118,"column":294},"action":"insert","lines":["my_exchanges_req_awaiting_confirmation"]}],[{"start":{"row":118,"column":297},"end":{"row":118,"column":332},"action":"remove","lines":["exchanges_req_awaiting_confirmation"],"id":117},{"start":{"row":118,"column":297},"end":{"row":118,"column":335},"action":"insert","lines":["my_exchanges_req_awaiting_confirmation"]}],[{"start":{"row":42,"column":91},"end":{"row":43,"column":0},"action":"insert","lines":["",""],"id":118},{"start":{"row":43,"column":0},"end":{"row":43,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":43,"column":12},"end":{"row":44,"column":68},"action":"insert","lines":["exch_shift = Shift.objects.get(shift_label=roster_day.roster_shift_label)","            newly_created_exch_req.exchanging_req_shift = exch_shift"],"id":119}],[{"start":{"row":149,"column":92},"end":{"row":150,"column":0},"action":"insert","lines":["",""],"id":120},{"start":{"row":150,"column":0},"end":{"row":150,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":150,"column":12},"end":{"row":151,"column":76},"action":"insert","lines":["replace_shift = Shift.objects.get(shift_label=roster_day.roster_shift_label)","            newly_created_exch_req_reply.replacing_req_shift = replace_shift"],"id":121}],[{"start":{"row":300,"column":45},"end":{"row":301,"column":0},"action":"insert","lines":["",""],"id":122},{"start":{"row":301,"column":0},"end":{"row":301,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":302,"column":188},"end":{"row":302,"column":208},"action":"insert","lines":["exchanging_req_shift"],"id":123}],[{"start":{"row":302,"column":208},"end":{"row":302,"column":209},"action":"insert","lines":["="],"id":124}],[{"start":{"row":302,"column":209},"end":{"row":302,"column":225},"action":"insert","lines":["shift_conversion"],"id":125}],[{"start":{"row":302,"column":225},"end":{"row":302,"column":226},"action":"insert","lines":[","],"id":126}],[{"start":{"row":302,"column":226},"end":{"row":302,"column":227},"action":"insert","lines":[" "],"id":127}],[{"start":{"row":149,"column":60},"end":{"row":149,"column":61},"action":"insert","lines":["_"],"id":128},{"start":{"row":149,"column":61},"end":{"row":149,"column":62},"action":"insert","lines":["l"]},{"start":{"row":149,"column":62},"end":{"row":149,"column":63},"action":"insert","lines":["a"]},{"start":{"row":149,"column":63},"end":{"row":149,"column":64},"action":"insert","lines":["b"]},{"start":{"row":149,"column":64},"end":{"row":149,"column":65},"action":"insert","lines":["e"]},{"start":{"row":149,"column":65},"end":{"row":149,"column":66},"action":"insert","lines":["l"]}]]},"ace":{"folds":[],"scrolltop":434,"scrollleft":0,"selection":{"start":{"row":31,"column":62},"end":{"row":31,"column":62},"isBackwards":true},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":187,"state":"start","mode":"ace/mode/python"}},"timestamp":1616254916846,"hash":"45a8084ecc3f3820dc5479824eeeb85841279602"}