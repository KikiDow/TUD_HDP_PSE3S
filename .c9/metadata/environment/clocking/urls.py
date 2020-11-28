{"filter":false,"title":"urls.py","tooltip":"/clocking/urls.py","undoManager":{"mark":76,"position":76,"stack":[[{"start":{"row":1,"column":82},"end":{"row":1,"column":83},"action":"insert","lines":[","],"id":28}],[{"start":{"row":1,"column":83},"end":{"row":1,"column":84},"action":"insert","lines":[" "],"id":29}],[{"start":{"row":1,"column":84},"end":{"row":1,"column":105},"action":"insert","lines":["view_personal_details"],"id":30}],[{"start":{"row":7,"column":68},"end":{"row":8,"column":0},"action":"insert","lines":["",""],"id":31},{"start":{"row":8,"column":0},"end":{"row":8,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":8,"column":4},"end":{"row":8,"column":90},"action":"insert","lines":["url(r'^view_personal_details/$', view_personal_details, name='view_personal_details'),"],"id":32}],[{"start":{"row":1,"column":105},"end":{"row":1,"column":106},"action":"insert","lines":[","],"id":33}],[{"start":{"row":1,"column":106},"end":{"row":1,"column":107},"action":"insert","lines":[" "],"id":34}],[{"start":{"row":1,"column":107},"end":{"row":1,"column":130},"action":"insert","lines":["create_personal_details"],"id":35}],[{"start":{"row":8,"column":90},"end":{"row":9,"column":0},"action":"insert","lines":["",""],"id":36},{"start":{"row":9,"column":0},"end":{"row":9,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":9,"column":4},"end":{"row":9,"column":96},"action":"insert","lines":["url(r'^create_personal_details/$', create_personal_details, name='create_personal_details'),"],"id":37}],[{"start":{"row":1,"column":130},"end":{"row":1,"column":131},"action":"insert","lines":[","],"id":38}],[{"start":{"row":1,"column":131},"end":{"row":1,"column":132},"action":"insert","lines":[" "],"id":39}],[{"start":{"row":1,"column":132},"end":{"row":1,"column":153},"action":"insert","lines":["edit_personal_details"],"id":40}],[{"start":{"row":9,"column":96},"end":{"row":10,"column":0},"action":"insert","lines":["",""],"id":41},{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":10,"column":4},"end":{"row":10,"column":102},"action":"insert","lines":["url(r'^(?P<pk>\\d+)/edit_personal_details/$', edit_personal_details, name='edit_personal_details'),"],"id":42}],[{"start":{"row":1,"column":153},"end":{"row":1,"column":154},"action":"insert","lines":[","],"id":43}],[{"start":{"row":1,"column":154},"end":{"row":1,"column":155},"action":"insert","lines":[" "],"id":44}],[{"start":{"row":1,"column":155},"end":{"row":1,"column":171},"action":"insert","lines":["my_notifications"],"id":45}],[{"start":{"row":10,"column":102},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":46},{"start":{"row":11,"column":0},"end":{"row":11,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":11,"column":4},"end":{"row":11,"column":71},"action":"insert","lines":["url(r'^notifications$', my_notifications, name='my_notifications'),"],"id":47}],[{"start":{"row":1,"column":171},"end":{"row":1,"column":172},"action":"insert","lines":[","],"id":48}],[{"start":{"row":1,"column":172},"end":{"row":1,"column":173},"action":"insert","lines":[" "],"id":49}],[{"start":{"row":1,"column":173},"end":{"row":1,"column":178},"action":"insert","lines":["clock"],"id":50}],[{"start":{"row":11,"column":71},"end":{"row":12,"column":0},"action":"insert","lines":["",""],"id":51},{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":12,"column":4},"end":{"row":12,"column":42},"action":"insert","lines":["url(r'^clock/$', clock, name='clock'),"],"id":52}],[{"start":{"row":1,"column":178},"end":{"row":1,"column":179},"action":"insert","lines":[","],"id":53}],[{"start":{"row":1,"column":179},"end":{"row":1,"column":180},"action":"insert","lines":[" "],"id":54}],[{"start":{"row":1,"column":180},"end":{"row":1,"column":195},"action":"insert","lines":["manual_clocking"],"id":55}],[{"start":{"row":12,"column":42},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":56},{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":13,"column":4},"end":{"row":13,"column":73},"action":"insert","lines":[" url(r'^manual_clocking/$', manual_clocking, name='manual_clocking'),"],"id":57}],[{"start":{"row":13,"column":4},"end":{"row":13,"column":5},"action":"remove","lines":[" "],"id":58}],[{"start":{"row":1,"column":195},"end":{"row":1,"column":196},"action":"insert","lines":[","],"id":59}],[{"start":{"row":1,"column":196},"end":{"row":1,"column":197},"action":"insert","lines":[" "],"id":60}],[{"start":{"row":1,"column":197},"end":{"row":1,"column":214},"action":"insert","lines":["view_manual_clock"],"id":61}],[{"start":{"row":13,"column":72},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":62},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":14,"column":4},"end":{"row":14,"column":72},"action":"insert","lines":["url(r'^(?P<pk>\\d+)/$', view_manual_clock, name='view_manual_clock'),"],"id":63}],[{"start":{"row":1,"column":214},"end":{"row":1,"column":215},"action":"insert","lines":[","],"id":64}],[{"start":{"row":1,"column":215},"end":{"row":1,"column":216},"action":"insert","lines":[" "],"id":65}],[{"start":{"row":1,"column":216},"end":{"row":1,"column":247},"action":"insert","lines":["view_submitted_manual_clockings"],"id":66}],[{"start":{"row":14,"column":72},"end":{"row":15,"column":0},"action":"insert","lines":["",""],"id":67},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":15,"column":4},"end":{"row":15,"column":120},"action":"insert","lines":["url(r'^view_submitted_manual_clockings/$', view_submitted_manual_clockings, name='view_submitted_manual_clockings'),"],"id":68}],[{"start":{"row":1,"column":247},"end":{"row":1,"column":248},"action":"insert","lines":[","],"id":69}],[{"start":{"row":1,"column":248},"end":{"row":1,"column":249},"action":"insert","lines":[" "],"id":70}],[{"start":{"row":1,"column":249},"end":{"row":1,"column":268},"action":"insert","lines":["accept_manual_clock"],"id":71}],[{"start":{"row":15,"column":120},"end":{"row":16,"column":0},"action":"insert","lines":["",""],"id":72},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":16,"column":4},"end":{"row":16,"column":96},"action":"insert","lines":["url(r'^(?P<pk>\\d+)/accept_manual_clock/$', accept_manual_clock, name='accept_manual_clock'),"],"id":73}],[{"start":{"row":1,"column":268},"end":{"row":1,"column":269},"action":"insert","lines":[","],"id":74}],[{"start":{"row":1,"column":269},"end":{"row":1,"column":270},"action":"insert","lines":[" "],"id":75}],[{"start":{"row":1,"column":270},"end":{"row":1,"column":289},"action":"insert","lines":["reject_manual_clock"],"id":76}],[{"start":{"row":16,"column":96},"end":{"row":17,"column":0},"action":"insert","lines":["",""],"id":77},{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":17,"column":4},"end":{"row":17,"column":96},"action":"insert","lines":["url(r'^(?P<pk>\\d+)/reject_manual_clock/$', reject_manual_clock, name='reject_manual_clock'),"],"id":78}],[{"start":{"row":1,"column":289},"end":{"row":1,"column":290},"action":"insert","lines":[","],"id":79}],[{"start":{"row":1,"column":290},"end":{"row":1,"column":291},"action":"insert","lines":[" "],"id":80}],[{"start":{"row":1,"column":291},"end":{"row":1,"column":304},"action":"insert","lines":["search_roster"],"id":81}],[{"start":{"row":17,"column":96},"end":{"row":18,"column":0},"action":"insert","lines":["",""],"id":82},{"start":{"row":18,"column":0},"end":{"row":18,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":18,"column":4},"end":{"row":18,"column":66},"action":"insert","lines":["url(r'^search_roster/$', search_roster, name='search_roster'),"],"id":83}],[{"start":{"row":1,"column":304},"end":{"row":1,"column":305},"action":"insert","lines":[","],"id":84}],[{"start":{"row":1,"column":305},"end":{"row":1,"column":306},"action":"insert","lines":[" "],"id":85}],[{"start":{"row":1,"column":306},"end":{"row":1,"column":331},"action":"insert","lines":["previous_manual_clockings"],"id":86}],[{"start":{"row":19,"column":1},"end":{"row":19,"column":26},"action":"insert","lines":["previous_manual_clockings"],"id":87}],[{"start":{"row":18,"column":66},"end":{"row":19,"column":0},"action":"insert","lines":["",""],"id":88},{"start":{"row":19,"column":0},"end":{"row":19,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":19,"column":4},"end":{"row":19,"column":66},"action":"insert","lines":["url(r'^search_roster/$', search_roster, name='search_roster'),"],"id":89}],[{"start":{"row":19,"column":11},"end":{"row":19,"column":24},"action":"remove","lines":["search_roster"],"id":90},{"start":{"row":19,"column":11},"end":{"row":19,"column":36},"action":"insert","lines":["previous_manual_clockings"]}],[{"start":{"row":19,"column":41},"end":{"row":19,"column":54},"action":"remove","lines":["search_roster"],"id":91},{"start":{"row":19,"column":41},"end":{"row":19,"column":66},"action":"insert","lines":["previous_manual_clockings"]}],[{"start":{"row":19,"column":74},"end":{"row":19,"column":87},"action":"remove","lines":["search_roster"],"id":92},{"start":{"row":19,"column":74},"end":{"row":19,"column":99},"action":"insert","lines":["previous_manual_clockings"]}],[{"start":{"row":20,"column":25},"end":{"row":20,"column":26},"action":"remove","lines":["s"],"id":93},{"start":{"row":20,"column":24},"end":{"row":20,"column":25},"action":"remove","lines":["g"]},{"start":{"row":20,"column":23},"end":{"row":20,"column":24},"action":"remove","lines":["n"]},{"start":{"row":20,"column":22},"end":{"row":20,"column":23},"action":"remove","lines":["i"]},{"start":{"row":20,"column":21},"end":{"row":20,"column":22},"action":"remove","lines":["k"]},{"start":{"row":20,"column":20},"end":{"row":20,"column":21},"action":"remove","lines":["c"]},{"start":{"row":20,"column":19},"end":{"row":20,"column":20},"action":"remove","lines":["o"]},{"start":{"row":20,"column":18},"end":{"row":20,"column":19},"action":"remove","lines":["l"]},{"start":{"row":20,"column":17},"end":{"row":20,"column":18},"action":"remove","lines":["c"]},{"start":{"row":20,"column":16},"end":{"row":20,"column":17},"action":"remove","lines":["_"]},{"start":{"row":20,"column":15},"end":{"row":20,"column":16},"action":"remove","lines":["l"]},{"start":{"row":20,"column":14},"end":{"row":20,"column":15},"action":"remove","lines":["a"]},{"start":{"row":20,"column":13},"end":{"row":20,"column":14},"action":"remove","lines":["u"]},{"start":{"row":20,"column":12},"end":{"row":20,"column":13},"action":"remove","lines":["n"]},{"start":{"row":20,"column":11},"end":{"row":20,"column":12},"action":"remove","lines":["a"]},{"start":{"row":20,"column":10},"end":{"row":20,"column":11},"action":"remove","lines":["m"]},{"start":{"row":20,"column":9},"end":{"row":20,"column":10},"action":"remove","lines":["_"]},{"start":{"row":20,"column":8},"end":{"row":20,"column":9},"action":"remove","lines":["s"]},{"start":{"row":20,"column":7},"end":{"row":20,"column":8},"action":"remove","lines":["u"]},{"start":{"row":20,"column":6},"end":{"row":20,"column":7},"action":"remove","lines":["o"]},{"start":{"row":20,"column":5},"end":{"row":20,"column":6},"action":"remove","lines":["i"]}],[{"start":{"row":20,"column":4},"end":{"row":20,"column":5},"action":"remove","lines":["v"],"id":94},{"start":{"row":20,"column":3},"end":{"row":20,"column":4},"action":"remove","lines":["e"]},{"start":{"row":20,"column":2},"end":{"row":20,"column":3},"action":"remove","lines":["r"]},{"start":{"row":20,"column":1},"end":{"row":20,"column":2},"action":"remove","lines":["p"]}],[{"start":{"row":1,"column":331},"end":{"row":1,"column":332},"action":"insert","lines":[","],"id":95}],[{"start":{"row":1,"column":332},"end":{"row":1,"column":333},"action":"insert","lines":[" "],"id":96}],[{"start":{"row":1,"column":333},"end":{"row":1,"column":353},"action":"insert","lines":["search_manual_clocks"],"id":97}],[{"start":{"row":20,"column":1},"end":{"row":20,"column":21},"action":"insert","lines":["search_manual_clocks"],"id":98}],[{"start":{"row":19,"column":102},"end":{"row":20,"column":0},"action":"insert","lines":["",""],"id":99},{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":20,"column":4},"end":{"row":20,"column":102},"action":"insert","lines":["url(r'^previous_manual_clockings/$', previous_manual_clockings, name='previous_manual_clockings'),"],"id":100}],[{"start":{"row":21,"column":1},"end":{"row":21,"column":21},"action":"remove","lines":["search_manual_clocks"],"id":101}],[{"start":{"row":20,"column":11},"end":{"row":20,"column":36},"action":"remove","lines":["previous_manual_clockings"],"id":102},{"start":{"row":20,"column":11},"end":{"row":20,"column":31},"action":"insert","lines":["search_manual_clocks"]}],[{"start":{"row":20,"column":36},"end":{"row":20,"column":61},"action":"remove","lines":["previous_manual_clockings"],"id":103},{"start":{"row":20,"column":36},"end":{"row":20,"column":56},"action":"insert","lines":["search_manual_clocks"]}],[{"start":{"row":20,"column":64},"end":{"row":20,"column":89},"action":"remove","lines":["previous_manual_clockings"],"id":104},{"start":{"row":20,"column":64},"end":{"row":20,"column":84},"action":"insert","lines":["search_manual_clocks"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":20,"column":11},"end":{"row":20,"column":31},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1606559843221,"hash":"e6f6d3a0162c40d9b75c8416ee76a5e0cf25289b"}