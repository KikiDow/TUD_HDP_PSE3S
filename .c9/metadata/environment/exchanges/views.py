{"filter":false,"title":"views.py","tooltip":"/exchanges/views.py","undoManager":{"mark":57,"position":57,"stack":[[{"start":{"row":132,"column":60},"end":{"row":133,"column":0},"action":"insert","lines":["",""],"id":170},{"start":{"row":133,"column":0},"end":{"row":133,"column":4},"action":"insert","lines":["    "]},{"start":{"row":133,"column":4},"end":{"row":134,"column":0},"action":"insert","lines":["",""]},{"start":{"row":134,"column":0},"end":{"row":134,"column":4},"action":"insert","lines":["    "]},{"start":{"row":134,"column":4},"end":{"row":134,"column":5},"action":"insert","lines":["#"]},{"start":{"row":134,"column":5},"end":{"row":134,"column":6},"action":"insert","lines":["P"]},{"start":{"row":134,"column":6},"end":{"row":134,"column":7},"action":"insert","lines":["a"]},{"start":{"row":134,"column":7},"end":{"row":134,"column":8},"action":"insert","lines":["g"]}],[{"start":{"row":134,"column":8},"end":{"row":134,"column":9},"action":"insert","lines":["i"],"id":171},{"start":{"row":134,"column":9},"end":{"row":134,"column":10},"action":"insert","lines":["n"]},{"start":{"row":134,"column":10},"end":{"row":134,"column":11},"action":"insert","lines":["a"]},{"start":{"row":134,"column":11},"end":{"row":134,"column":12},"action":"insert","lines":["t"]},{"start":{"row":134,"column":12},"end":{"row":134,"column":13},"action":"insert","lines":["i"]},{"start":{"row":134,"column":13},"end":{"row":134,"column":14},"action":"insert","lines":["o"]},{"start":{"row":134,"column":14},"end":{"row":134,"column":15},"action":"insert","lines":["n"]}],[{"start":{"row":134,"column":15},"end":{"row":134,"column":16},"action":"insert","lines":[" "],"id":172},{"start":{"row":134,"column":16},"end":{"row":134,"column":17},"action":"insert","lines":["f"]},{"start":{"row":134,"column":17},"end":{"row":134,"column":18},"action":"insert","lines":["o"]}],[{"start":{"row":134,"column":18},"end":{"row":134,"column":19},"action":"insert","lines":[" "],"id":173}],[{"start":{"row":134,"column":18},"end":{"row":134,"column":19},"action":"remove","lines":[" "],"id":174}],[{"start":{"row":134,"column":18},"end":{"row":134,"column":19},"action":"insert","lines":["r"],"id":175}],[{"start":{"row":134,"column":19},"end":{"row":134,"column":20},"action":"insert","lines":[" "],"id":176},{"start":{"row":134,"column":20},"end":{"row":134,"column":21},"action":"insert","lines":["p"]},{"start":{"row":134,"column":21},"end":{"row":134,"column":22},"action":"insert","lines":["r"]},{"start":{"row":134,"column":22},"end":{"row":134,"column":23},"action":"insert","lines":["e"]},{"start":{"row":134,"column":23},"end":{"row":134,"column":24},"action":"insert","lines":["v"]},{"start":{"row":134,"column":24},"end":{"row":134,"column":25},"action":"insert","lines":["i"]},{"start":{"row":134,"column":25},"end":{"row":134,"column":26},"action":"insert","lines":["o"]},{"start":{"row":134,"column":26},"end":{"row":134,"column":27},"action":"insert","lines":["u"]},{"start":{"row":134,"column":27},"end":{"row":134,"column":28},"action":"insert","lines":["s"]}],[{"start":{"row":134,"column":28},"end":{"row":134,"column":29},"action":"insert","lines":[" "],"id":177},{"start":{"row":134,"column":29},"end":{"row":134,"column":30},"action":"insert","lines":["e"]},{"start":{"row":134,"column":30},"end":{"row":134,"column":31},"action":"insert","lines":["x"]},{"start":{"row":134,"column":31},"end":{"row":134,"column":32},"action":"insert","lines":["c"]},{"start":{"row":134,"column":32},"end":{"row":134,"column":33},"action":"insert","lines":["h"]},{"start":{"row":134,"column":33},"end":{"row":134,"column":34},"action":"insert","lines":["a"]}],[{"start":{"row":134,"column":34},"end":{"row":134,"column":35},"action":"insert","lines":["g"],"id":178}],[{"start":{"row":134,"column":34},"end":{"row":134,"column":35},"action":"remove","lines":["g"],"id":179}],[{"start":{"row":134,"column":34},"end":{"row":134,"column":35},"action":"insert","lines":["n"],"id":180},{"start":{"row":134,"column":35},"end":{"row":134,"column":36},"action":"insert","lines":["g"]},{"start":{"row":134,"column":36},"end":{"row":134,"column":37},"action":"insert","lines":["e"]},{"start":{"row":134,"column":37},"end":{"row":134,"column":38},"action":"insert","lines":["s"]}],[{"start":{"row":134,"column":38},"end":{"row":134,"column":39},"action":"insert","lines":["."],"id":181}],[{"start":{"row":134,"column":39},"end":{"row":135,"column":0},"action":"insert","lines":["",""],"id":182},{"start":{"row":135,"column":0},"end":{"row":135,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":135,"column":4},"end":{"row":144,"column":156},"action":"insert","lines":["exchanges_req_awaiting_confirmation_page_number = 1","    exchanges_req_awaiting_confirmation_page = request.GET.get('exchanges_req_awaiting_confirmation_page', exchanges_req_awaiting_confirmation_page_number)","    ","    exchanges_req_awaiting_confirmation_paginator = Paginator(exchanges_req_awaiting_confirmation, 3)","    try:","        my_exchanges_req_awaiting_confirmation = exchanges_req_awaiting_confirmation_paginator.page(exchanges_req_awaiting_confirmation_page)","    except PageNotAnInteger:","        my_exchanges_req_awaiting_confirmation = exchanges_req_awaiting_confirmation_paginator.page(1)","    except EmptyPage:","        my_exchanges_req_awaiting_confirmation = exchanges_req_awaiting_confirmation_paginator.page(exchanges_req_awaiting_confirmation_paginator.num_pages)"],"id":183}],[{"start":{"row":135,"column":38},"end":{"row":135,"column":39},"action":"remove","lines":["n"],"id":184},{"start":{"row":135,"column":37},"end":{"row":135,"column":38},"action":"remove","lines":["o"]},{"start":{"row":135,"column":36},"end":{"row":135,"column":37},"action":"remove","lines":["i"]},{"start":{"row":135,"column":35},"end":{"row":135,"column":36},"action":"remove","lines":["t"]},{"start":{"row":135,"column":34},"end":{"row":135,"column":35},"action":"remove","lines":["a"]},{"start":{"row":135,"column":33},"end":{"row":135,"column":34},"action":"remove","lines":["m"]},{"start":{"row":135,"column":32},"end":{"row":135,"column":33},"action":"remove","lines":["r"]},{"start":{"row":135,"column":31},"end":{"row":135,"column":32},"action":"remove","lines":["i"]},{"start":{"row":135,"column":30},"end":{"row":135,"column":31},"action":"remove","lines":["f"]},{"start":{"row":135,"column":29},"end":{"row":135,"column":30},"action":"remove","lines":["n"]},{"start":{"row":135,"column":28},"end":{"row":135,"column":29},"action":"remove","lines":["o"]},{"start":{"row":135,"column":27},"end":{"row":135,"column":28},"action":"remove","lines":["c"]},{"start":{"row":135,"column":26},"end":{"row":135,"column":27},"action":"remove","lines":["_"]},{"start":{"row":135,"column":25},"end":{"row":135,"column":26},"action":"remove","lines":["g"]},{"start":{"row":135,"column":24},"end":{"row":135,"column":25},"action":"remove","lines":["n"]},{"start":{"row":135,"column":23},"end":{"row":135,"column":24},"action":"remove","lines":["i"]},{"start":{"row":135,"column":22},"end":{"row":135,"column":23},"action":"remove","lines":["t"]},{"start":{"row":135,"column":21},"end":{"row":135,"column":22},"action":"remove","lines":["i"]},{"start":{"row":135,"column":20},"end":{"row":135,"column":21},"action":"remove","lines":["a"]},{"start":{"row":135,"column":19},"end":{"row":135,"column":20},"action":"remove","lines":["w"]},{"start":{"row":135,"column":18},"end":{"row":135,"column":19},"action":"remove","lines":["a"]},{"start":{"row":135,"column":17},"end":{"row":135,"column":18},"action":"remove","lines":["_"]},{"start":{"row":135,"column":16},"end":{"row":135,"column":17},"action":"remove","lines":["q"]},{"start":{"row":135,"column":15},"end":{"row":135,"column":16},"action":"remove","lines":["e"]},{"start":{"row":135,"column":14},"end":{"row":135,"column":15},"action":"remove","lines":["r"]},{"start":{"row":135,"column":13},"end":{"row":135,"column":14},"action":"remove","lines":["_"]},{"start":{"row":135,"column":12},"end":{"row":135,"column":13},"action":"remove","lines":["s"]},{"start":{"row":135,"column":11},"end":{"row":135,"column":12},"action":"remove","lines":["e"]},{"start":{"row":135,"column":10},"end":{"row":135,"column":11},"action":"remove","lines":["g"]},{"start":{"row":135,"column":9},"end":{"row":135,"column":10},"action":"remove","lines":["n"]},{"start":{"row":135,"column":8},"end":{"row":135,"column":9},"action":"remove","lines":["a"]},{"start":{"row":135,"column":7},"end":{"row":135,"column":8},"action":"remove","lines":["h"]},{"start":{"row":135,"column":6},"end":{"row":135,"column":7},"action":"remove","lines":["c"]},{"start":{"row":135,"column":5},"end":{"row":135,"column":6},"action":"remove","lines":["x"]}],[{"start":{"row":135,"column":4},"end":{"row":135,"column":5},"action":"remove","lines":["e"],"id":185}],[{"start":{"row":135,"column":4},"end":{"row":135,"column":5},"action":"insert","lines":["p"],"id":186},{"start":{"row":135,"column":5},"end":{"row":135,"column":6},"action":"insert","lines":["r"]},{"start":{"row":135,"column":6},"end":{"row":135,"column":7},"action":"insert","lines":["e"]},{"start":{"row":135,"column":7},"end":{"row":135,"column":8},"action":"insert","lines":["v"]},{"start":{"row":135,"column":8},"end":{"row":135,"column":9},"action":"insert","lines":["i"]},{"start":{"row":135,"column":9},"end":{"row":135,"column":10},"action":"insert","lines":["o"]},{"start":{"row":135,"column":10},"end":{"row":135,"column":11},"action":"insert","lines":["u"]},{"start":{"row":135,"column":11},"end":{"row":135,"column":12},"action":"insert","lines":["s"]}],[{"start":{"row":135,"column":12},"end":{"row":135,"column":13},"action":"insert","lines":["_"],"id":187},{"start":{"row":135,"column":13},"end":{"row":135,"column":14},"action":"insert","lines":["e"]},{"start":{"row":135,"column":14},"end":{"row":135,"column":15},"action":"insert","lines":["x"]},{"start":{"row":135,"column":15},"end":{"row":135,"column":16},"action":"insert","lines":["c"]},{"start":{"row":135,"column":16},"end":{"row":135,"column":17},"action":"insert","lines":["h"]}],[{"start":{"row":136,"column":4},"end":{"row":136,"column":39},"action":"remove","lines":["exchanges_req_awaiting_confirmation"],"id":188},{"start":{"row":136,"column":4},"end":{"row":136,"column":17},"action":"insert","lines":["previous_exch"]}],[{"start":{"row":136,"column":42},"end":{"row":136,"column":77},"action":"remove","lines":["exchanges_req_awaiting_confirmation"],"id":189},{"start":{"row":136,"column":42},"end":{"row":136,"column":55},"action":"insert","lines":["previous_exch"]}],[{"start":{"row":136,"column":63},"end":{"row":136,"column":98},"action":"remove","lines":["exchanges_req_awaiting_confirmation"],"id":190},{"start":{"row":136,"column":63},"end":{"row":136,"column":76},"action":"insert","lines":["previous_exch"]}],[{"start":{"row":138,"column":4},"end":{"row":138,"column":39},"action":"remove","lines":["exchanges_req_awaiting_confirmation"],"id":191},{"start":{"row":138,"column":4},"end":{"row":138,"column":17},"action":"insert","lines":["previous_exch"]}],[{"start":{"row":138,"column":77},"end":{"row":138,"column":78},"action":"remove","lines":["3"],"id":192}],[{"start":{"row":138,"column":77},"end":{"row":138,"column":78},"action":"insert","lines":["6"],"id":193}],[{"start":{"row":138,"column":40},"end":{"row":138,"column":75},"action":"remove","lines":["exchanges_req_awaiting_confirmation"],"id":194},{"start":{"row":138,"column":40},"end":{"row":138,"column":62},"action":"insert","lines":["previous_exchange_reqs"]}],[{"start":{"row":140,"column":11},"end":{"row":140,"column":46},"action":"remove","lines":["exchanges_req_awaiting_confirmation"],"id":195},{"start":{"row":140,"column":11},"end":{"row":140,"column":12},"action":"insert","lines":["p"]},{"start":{"row":140,"column":12},"end":{"row":140,"column":13},"action":"insert","lines":["r"]},{"start":{"row":140,"column":13},"end":{"row":140,"column":14},"action":"insert","lines":["e"]},{"start":{"row":140,"column":14},"end":{"row":140,"column":15},"action":"insert","lines":["v"]},{"start":{"row":140,"column":15},"end":{"row":140,"column":16},"action":"insert","lines":["i"]},{"start":{"row":140,"column":16},"end":{"row":140,"column":17},"action":"insert","lines":["o"]},{"start":{"row":140,"column":17},"end":{"row":140,"column":18},"action":"insert","lines":["u"]},{"start":{"row":140,"column":18},"end":{"row":140,"column":19},"action":"insert","lines":["s"]},{"start":{"row":140,"column":19},"end":{"row":140,"column":20},"action":"insert","lines":["_"]}],[{"start":{"row":140,"column":20},"end":{"row":140,"column":21},"action":"insert","lines":["e"],"id":196},{"start":{"row":140,"column":21},"end":{"row":140,"column":22},"action":"insert","lines":["x"]},{"start":{"row":140,"column":22},"end":{"row":140,"column":23},"action":"insert","lines":["c"]},{"start":{"row":140,"column":23},"end":{"row":140,"column":24},"action":"insert","lines":["h"]},{"start":{"row":140,"column":24},"end":{"row":140,"column":25},"action":"insert","lines":["a"]},{"start":{"row":140,"column":25},"end":{"row":140,"column":26},"action":"insert","lines":["n"]},{"start":{"row":140,"column":26},"end":{"row":140,"column":27},"action":"insert","lines":["g"]},{"start":{"row":140,"column":27},"end":{"row":140,"column":28},"action":"insert","lines":["e"]},{"start":{"row":140,"column":28},"end":{"row":140,"column":29},"action":"insert","lines":["s"]}],[{"start":{"row":142,"column":11},"end":{"row":142,"column":46},"action":"remove","lines":["exchanges_req_awaiting_confirmation"],"id":197},{"start":{"row":142,"column":11},"end":{"row":142,"column":29},"action":"insert","lines":["previous_exchanges"]}],[{"start":{"row":144,"column":11},"end":{"row":144,"column":46},"action":"remove","lines":["exchanges_req_awaiting_confirmation"],"id":198},{"start":{"row":144,"column":11},"end":{"row":144,"column":29},"action":"insert","lines":["previous_exchanges"]}],[{"start":{"row":140,"column":32},"end":{"row":140,"column":67},"action":"remove","lines":["exchanges_req_awaiting_confirmation"],"id":199},{"start":{"row":140,"column":32},"end":{"row":140,"column":45},"action":"insert","lines":["previous_exch"]}],[{"start":{"row":142,"column":32},"end":{"row":142,"column":67},"action":"remove","lines":["exchanges_req_awaiting_confirmation"],"id":200},{"start":{"row":142,"column":32},"end":{"row":142,"column":45},"action":"insert","lines":["previous_exch"]}],[{"start":{"row":144,"column":32},"end":{"row":144,"column":67},"action":"remove","lines":["exchanges_req_awaiting_confirmation"],"id":201},{"start":{"row":144,"column":32},"end":{"row":144,"column":45},"action":"insert","lines":["previous_exch"]}],[{"start":{"row":144,"column":61},"end":{"row":144,"column":96},"action":"remove","lines":["exchanges_req_awaiting_confirmation"],"id":202},{"start":{"row":144,"column":61},"end":{"row":144,"column":74},"action":"insert","lines":["previous_exch"]}],[{"start":{"row":140,"column":61},"end":{"row":140,"column":101},"action":"remove","lines":["exchanges_req_awaiting_confirmation_page"],"id":203},{"start":{"row":140,"column":61},"end":{"row":140,"column":79},"action":"insert","lines":["previous_exch_page"]}],[{"start":{"row":146,"column":113},"end":{"row":146,"column":135},"action":"remove","lines":["previous_exchange_reqs"],"id":204},{"start":{"row":146,"column":113},"end":{"row":146,"column":134},"action":"insert","lines":["my_previous_exchanges"]}],[{"start":{"row":146,"column":137},"end":{"row":146,"column":159},"action":"remove","lines":["previous_exchange_reqs"],"id":205},{"start":{"row":146,"column":137},"end":{"row":146,"column":158},"action":"insert","lines":["my_previous_exchanges"]}],[{"start":{"row":144,"column":95},"end":{"row":145,"column":0},"action":"insert","lines":["",""],"id":206},{"start":{"row":145,"column":0},"end":{"row":145,"column":8},"action":"insert","lines":["        "]},{"start":{"row":145,"column":8},"end":{"row":146,"column":0},"action":"insert","lines":["",""]},{"start":{"row":146,"column":0},"end":{"row":146,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":146,"column":4},"end":{"row":146,"column":8},"action":"remove","lines":["    "],"id":207}],[{"start":{"row":146,"column":4},"end":{"row":156,"column":95},"action":"insert","lines":["#Pagination for previous exchanges.","    previous_exch_page_number = 1","    previous_exch_page = request.GET.get('previous_exch_page', previous_exch_page_number)","    ","    previous_exch_paginator = Paginator(previous_exchange_reqs, 6)","    try:","        my_previous_exchanges = previous_exch_paginator.page(previous_exch_page)","    except PageNotAnInteger:","        my_previous_exchanges = previous_exch_paginator.page(1)","    except EmptyPage:","        my_previous_exchanges = previous_exch_paginator.page(previous_exch_paginator.num_pages)"],"id":208}],[{"start":{"row":146,"column":27},"end":{"row":146,"column":28},"action":"remove","lines":["s"],"id":209},{"start":{"row":146,"column":26},"end":{"row":146,"column":27},"action":"remove","lines":["u"]},{"start":{"row":146,"column":25},"end":{"row":146,"column":26},"action":"remove","lines":["o"]},{"start":{"row":146,"column":24},"end":{"row":146,"column":25},"action":"remove","lines":["i"]},{"start":{"row":146,"column":23},"end":{"row":146,"column":24},"action":"remove","lines":["v"]},{"start":{"row":146,"column":22},"end":{"row":146,"column":23},"action":"remove","lines":["e"]},{"start":{"row":146,"column":21},"end":{"row":146,"column":22},"action":"remove","lines":["r"]},{"start":{"row":146,"column":20},"end":{"row":146,"column":21},"action":"remove","lines":["p"]}],[{"start":{"row":146,"column":20},"end":{"row":146,"column":21},"action":"insert","lines":["c"],"id":210},{"start":{"row":146,"column":21},"end":{"row":146,"column":22},"action":"insert","lines":["a"]},{"start":{"row":146,"column":22},"end":{"row":146,"column":23},"action":"insert","lines":["n"]},{"start":{"row":146,"column":23},"end":{"row":146,"column":24},"action":"insert","lines":["c"]},{"start":{"row":146,"column":24},"end":{"row":146,"column":25},"action":"insert","lines":["e"]},{"start":{"row":146,"column":25},"end":{"row":146,"column":26},"action":"insert","lines":["l"]},{"start":{"row":146,"column":26},"end":{"row":146,"column":27},"action":"insert","lines":["l"]},{"start":{"row":146,"column":27},"end":{"row":146,"column":28},"action":"insert","lines":["e"]},{"start":{"row":146,"column":28},"end":{"row":146,"column":29},"action":"insert","lines":["d"]}],[{"start":{"row":147,"column":11},"end":{"row":147,"column":12},"action":"remove","lines":["s"],"id":211},{"start":{"row":147,"column":10},"end":{"row":147,"column":11},"action":"remove","lines":["u"]},{"start":{"row":147,"column":9},"end":{"row":147,"column":10},"action":"remove","lines":["o"]},{"start":{"row":147,"column":8},"end":{"row":147,"column":9},"action":"remove","lines":["i"]},{"start":{"row":147,"column":7},"end":{"row":147,"column":8},"action":"remove","lines":["v"]},{"start":{"row":147,"column":6},"end":{"row":147,"column":7},"action":"remove","lines":["e"]},{"start":{"row":147,"column":5},"end":{"row":147,"column":6},"action":"remove","lines":["r"]},{"start":{"row":147,"column":4},"end":{"row":147,"column":5},"action":"remove","lines":["p"]}],[{"start":{"row":147,"column":4},"end":{"row":147,"column":5},"action":"insert","lines":["c"],"id":212},{"start":{"row":147,"column":5},"end":{"row":147,"column":6},"action":"insert","lines":["a"]},{"start":{"row":147,"column":6},"end":{"row":147,"column":7},"action":"insert","lines":["n"]},{"start":{"row":147,"column":7},"end":{"row":147,"column":8},"action":"insert","lines":["c"]},{"start":{"row":147,"column":8},"end":{"row":147,"column":9},"action":"insert","lines":["e"]},{"start":{"row":147,"column":9},"end":{"row":147,"column":10},"action":"insert","lines":["l"]},{"start":{"row":147,"column":10},"end":{"row":147,"column":11},"action":"insert","lines":["l"]},{"start":{"row":147,"column":11},"end":{"row":147,"column":12},"action":"insert","lines":["e"]},{"start":{"row":147,"column":12},"end":{"row":147,"column":13},"action":"insert","lines":["d"]}],[{"start":{"row":148,"column":4},"end":{"row":148,"column":12},"action":"remove","lines":["previous"],"id":213},{"start":{"row":148,"column":4},"end":{"row":148,"column":13},"action":"insert","lines":["cancelled"]}],[{"start":{"row":148,"column":43},"end":{"row":148,"column":51},"action":"remove","lines":["previous"],"id":214},{"start":{"row":148,"column":43},"end":{"row":148,"column":52},"action":"insert","lines":["cancelled"]}],[{"start":{"row":148,"column":65},"end":{"row":148,"column":73},"action":"remove","lines":["previous"],"id":215},{"start":{"row":148,"column":65},"end":{"row":148,"column":74},"action":"insert","lines":["cancelled"]}],[{"start":{"row":150,"column":4},"end":{"row":150,"column":12},"action":"remove","lines":["previous"],"id":216},{"start":{"row":150,"column":4},"end":{"row":150,"column":13},"action":"insert","lines":["cancelled"]}],[{"start":{"row":150,"column":41},"end":{"row":150,"column":63},"action":"remove","lines":["previous_exchange_reqs"],"id":217},{"start":{"row":150,"column":41},"end":{"row":150,"column":64},"action":"insert","lines":["exchange_reqs_cancelled"]}],[{"start":{"row":152,"column":11},"end":{"row":152,"column":19},"action":"remove","lines":["previous"],"id":218},{"start":{"row":152,"column":11},"end":{"row":152,"column":20},"action":"insert","lines":["cancelled"]}],[{"start":{"row":152,"column":33},"end":{"row":152,"column":41},"action":"remove","lines":["previous"],"id":219},{"start":{"row":152,"column":33},"end":{"row":152,"column":42},"action":"insert","lines":["cancelled"]}],[{"start":{"row":152,"column":63},"end":{"row":152,"column":71},"action":"remove","lines":["previous"],"id":220},{"start":{"row":152,"column":63},"end":{"row":152,"column":72},"action":"insert","lines":["cancelled"]}],[{"start":{"row":154,"column":11},"end":{"row":154,"column":19},"action":"remove","lines":["previous"],"id":221},{"start":{"row":154,"column":11},"end":{"row":154,"column":20},"action":"insert","lines":["cancelled"]}],[{"start":{"row":154,"column":33},"end":{"row":154,"column":41},"action":"remove","lines":["previous"],"id":222},{"start":{"row":154,"column":33},"end":{"row":154,"column":42},"action":"insert","lines":["cancelled"]}],[{"start":{"row":156,"column":11},"end":{"row":156,"column":19},"action":"remove","lines":["previous"],"id":223},{"start":{"row":156,"column":11},"end":{"row":156,"column":20},"action":"insert","lines":["cancelled"]}],[{"start":{"row":156,"column":33},"end":{"row":156,"column":41},"action":"remove","lines":["previous"],"id":224},{"start":{"row":156,"column":33},"end":{"row":156,"column":42},"action":"insert","lines":["cancelled"]}],[{"start":{"row":156,"column":63},"end":{"row":156,"column":71},"action":"remove","lines":["previous"],"id":225},{"start":{"row":156,"column":63},"end":{"row":156,"column":72},"action":"insert","lines":["cancelled"]}],[{"start":{"row":158,"column":61},"end":{"row":158,"column":84},"action":"remove","lines":["exchange_reqs_cancelled"],"id":226},{"start":{"row":158,"column":61},"end":{"row":158,"column":83},"action":"insert","lines":["my_cancelled_exchanges"]}],[{"start":{"row":158,"column":86},"end":{"row":158,"column":109},"action":"remove","lines":["exchange_reqs_cancelled"],"id":227},{"start":{"row":158,"column":86},"end":{"row":158,"column":108},"action":"insert","lines":["my_cancelled_exchanges"]}]]},"ace":{"folds":[],"scrolltop":1951,"scrollleft":0,"selection":{"start":{"row":148,"column":4},"end":{"row":148,"column":23},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":107,"state":"start","mode":"ace/mode/python"}},"timestamp":1617372504961,"hash":"dcb8b93ac9cfca0c728a1b419d478cd35d92365f"}