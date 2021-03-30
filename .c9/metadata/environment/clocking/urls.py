{"filter":false,"title":"urls.py","tooltip":"/clocking/urls.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":1,"column":196},"end":{"row":1,"column":197},"action":"insert","lines":[" "],"id":60}],[{"start":{"row":1,"column":197},"end":{"row":1,"column":214},"action":"insert","lines":["view_manual_clock"],"id":61}],[{"start":{"row":13,"column":72},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":62},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":14,"column":4},"end":{"row":14,"column":72},"action":"insert","lines":["url(r'^(?P<pk>\\d+)/$', view_manual_clock, name='view_manual_clock'),"],"id":63}],[{"start":{"row":1,"column":214},"end":{"row":1,"column":215},"action":"insert","lines":[","],"id":64}],[{"start":{"row":1,"column":215},"end":{"row":1,"column":216},"action":"insert","lines":[" "],"id":65}],[{"start":{"row":1,"column":216},"end":{"row":1,"column":247},"action":"insert","lines":["view_submitted_manual_clockings"],"id":66}],[{"start":{"row":14,"column":72},"end":{"row":15,"column":0},"action":"insert","lines":["",""],"id":67},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":15,"column":4},"end":{"row":15,"column":120},"action":"insert","lines":["url(r'^view_submitted_manual_clockings/$', view_submitted_manual_clockings, name='view_submitted_manual_clockings'),"],"id":68}],[{"start":{"row":1,"column":247},"end":{"row":1,"column":248},"action":"insert","lines":[","],"id":69}],[{"start":{"row":1,"column":248},"end":{"row":1,"column":249},"action":"insert","lines":[" "],"id":70}],[{"start":{"row":1,"column":249},"end":{"row":1,"column":268},"action":"insert","lines":["accept_manual_clock"],"id":71}],[{"start":{"row":15,"column":120},"end":{"row":16,"column":0},"action":"insert","lines":["",""],"id":72},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":16,"column":4},"end":{"row":16,"column":96},"action":"insert","lines":["url(r'^(?P<pk>\\d+)/accept_manual_clock/$', accept_manual_clock, name='accept_manual_clock'),"],"id":73}],[{"start":{"row":1,"column":268},"end":{"row":1,"column":269},"action":"insert","lines":[","],"id":74}],[{"start":{"row":1,"column":269},"end":{"row":1,"column":270},"action":"insert","lines":[" "],"id":75}],[{"start":{"row":1,"column":270},"end":{"row":1,"column":289},"action":"insert","lines":["reject_manual_clock"],"id":76}],[{"start":{"row":16,"column":96},"end":{"row":17,"column":0},"action":"insert","lines":["",""],"id":77},{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":17,"column":4},"end":{"row":17,"column":96},"action":"insert","lines":["url(r'^(?P<pk>\\d+)/reject_manual_clock/$', reject_manual_clock, name='reject_manual_clock'),"],"id":78}],[{"start":{"row":1,"column":289},"end":{"row":1,"column":290},"action":"insert","lines":[","],"id":79}],[{"start":{"row":1,"column":290},"end":{"row":1,"column":291},"action":"insert","lines":[" "],"id":80}],[{"start":{"row":1,"column":291},"end":{"row":1,"column":304},"action":"insert","lines":["search_roster"],"id":81}],[{"start":{"row":17,"column":96},"end":{"row":18,"column":0},"action":"insert","lines":["",""],"id":82},{"start":{"row":18,"column":0},"end":{"row":18,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":18,"column":4},"end":{"row":18,"column":66},"action":"insert","lines":["url(r'^search_roster/$', search_roster, name='search_roster'),"],"id":83}],[{"start":{"row":1,"column":304},"end":{"row":1,"column":305},"action":"insert","lines":[","],"id":84}],[{"start":{"row":1,"column":305},"end":{"row":1,"column":306},"action":"insert","lines":[" "],"id":85}],[{"start":{"row":1,"column":306},"end":{"row":1,"column":331},"action":"insert","lines":["previous_manual_clockings"],"id":86}],[{"start":{"row":19,"column":1},"end":{"row":19,"column":26},"action":"insert","lines":["previous_manual_clockings"],"id":87}],[{"start":{"row":18,"column":66},"end":{"row":19,"column":0},"action":"insert","lines":["",""],"id":88},{"start":{"row":19,"column":0},"end":{"row":19,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":19,"column":4},"end":{"row":19,"column":66},"action":"insert","lines":["url(r'^search_roster/$', search_roster, name='search_roster'),"],"id":89}],[{"start":{"row":19,"column":11},"end":{"row":19,"column":24},"action":"remove","lines":["search_roster"],"id":90},{"start":{"row":19,"column":11},"end":{"row":19,"column":36},"action":"insert","lines":["previous_manual_clockings"]}],[{"start":{"row":19,"column":41},"end":{"row":19,"column":54},"action":"remove","lines":["search_roster"],"id":91},{"start":{"row":19,"column":41},"end":{"row":19,"column":66},"action":"insert","lines":["previous_manual_clockings"]}],[{"start":{"row":19,"column":74},"end":{"row":19,"column":87},"action":"remove","lines":["search_roster"],"id":92},{"start":{"row":19,"column":74},"end":{"row":19,"column":99},"action":"insert","lines":["previous_manual_clockings"]}],[{"start":{"row":20,"column":25},"end":{"row":20,"column":26},"action":"remove","lines":["s"],"id":93},{"start":{"row":20,"column":24},"end":{"row":20,"column":25},"action":"remove","lines":["g"]},{"start":{"row":20,"column":23},"end":{"row":20,"column":24},"action":"remove","lines":["n"]},{"start":{"row":20,"column":22},"end":{"row":20,"column":23},"action":"remove","lines":["i"]},{"start":{"row":20,"column":21},"end":{"row":20,"column":22},"action":"remove","lines":["k"]},{"start":{"row":20,"column":20},"end":{"row":20,"column":21},"action":"remove","lines":["c"]},{"start":{"row":20,"column":19},"end":{"row":20,"column":20},"action":"remove","lines":["o"]},{"start":{"row":20,"column":18},"end":{"row":20,"column":19},"action":"remove","lines":["l"]},{"start":{"row":20,"column":17},"end":{"row":20,"column":18},"action":"remove","lines":["c"]},{"start":{"row":20,"column":16},"end":{"row":20,"column":17},"action":"remove","lines":["_"]},{"start":{"row":20,"column":15},"end":{"row":20,"column":16},"action":"remove","lines":["l"]},{"start":{"row":20,"column":14},"end":{"row":20,"column":15},"action":"remove","lines":["a"]},{"start":{"row":20,"column":13},"end":{"row":20,"column":14},"action":"remove","lines":["u"]},{"start":{"row":20,"column":12},"end":{"row":20,"column":13},"action":"remove","lines":["n"]},{"start":{"row":20,"column":11},"end":{"row":20,"column":12},"action":"remove","lines":["a"]},{"start":{"row":20,"column":10},"end":{"row":20,"column":11},"action":"remove","lines":["m"]},{"start":{"row":20,"column":9},"end":{"row":20,"column":10},"action":"remove","lines":["_"]},{"start":{"row":20,"column":8},"end":{"row":20,"column":9},"action":"remove","lines":["s"]},{"start":{"row":20,"column":7},"end":{"row":20,"column":8},"action":"remove","lines":["u"]},{"start":{"row":20,"column":6},"end":{"row":20,"column":7},"action":"remove","lines":["o"]},{"start":{"row":20,"column":5},"end":{"row":20,"column":6},"action":"remove","lines":["i"]}],[{"start":{"row":20,"column":4},"end":{"row":20,"column":5},"action":"remove","lines":["v"],"id":94},{"start":{"row":20,"column":3},"end":{"row":20,"column":4},"action":"remove","lines":["e"]},{"start":{"row":20,"column":2},"end":{"row":20,"column":3},"action":"remove","lines":["r"]},{"start":{"row":20,"column":1},"end":{"row":20,"column":2},"action":"remove","lines":["p"]}],[{"start":{"row":1,"column":331},"end":{"row":1,"column":332},"action":"insert","lines":[","],"id":95}],[{"start":{"row":1,"column":332},"end":{"row":1,"column":333},"action":"insert","lines":[" "],"id":96}],[{"start":{"row":1,"column":333},"end":{"row":1,"column":353},"action":"insert","lines":["search_manual_clocks"],"id":97}],[{"start":{"row":20,"column":1},"end":{"row":20,"column":21},"action":"insert","lines":["search_manual_clocks"],"id":98}],[{"start":{"row":19,"column":102},"end":{"row":20,"column":0},"action":"insert","lines":["",""],"id":99},{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":20,"column":4},"end":{"row":20,"column":102},"action":"insert","lines":["url(r'^previous_manual_clockings/$', previous_manual_clockings, name='previous_manual_clockings'),"],"id":100}],[{"start":{"row":21,"column":1},"end":{"row":21,"column":21},"action":"remove","lines":["search_manual_clocks"],"id":101}],[{"start":{"row":20,"column":11},"end":{"row":20,"column":36},"action":"remove","lines":["previous_manual_clockings"],"id":102},{"start":{"row":20,"column":11},"end":{"row":20,"column":31},"action":"insert","lines":["search_manual_clocks"]}],[{"start":{"row":20,"column":36},"end":{"row":20,"column":61},"action":"remove","lines":["previous_manual_clockings"],"id":103},{"start":{"row":20,"column":36},"end":{"row":20,"column":56},"action":"insert","lines":["search_manual_clocks"]}],[{"start":{"row":20,"column":64},"end":{"row":20,"column":89},"action":"remove","lines":["previous_manual_clockings"],"id":104},{"start":{"row":20,"column":64},"end":{"row":20,"column":84},"action":"insert","lines":["search_manual_clocks"]}],[{"start":{"row":14,"column":22},"end":{"row":14,"column":23},"action":"insert","lines":["/"],"id":105}],[{"start":{"row":14,"column":23},"end":{"row":14,"column":40},"action":"insert","lines":["view_manual_clock"],"id":106}],[{"start":{"row":1,"column":353},"end":{"row":1,"column":354},"action":"insert","lines":[","],"id":107}],[{"start":{"row":1,"column":354},"end":{"row":1,"column":355},"action":"insert","lines":[" "],"id":108}],[{"start":{"row":1,"column":355},"end":{"row":1,"column":372},"action":"insert","lines":["edit_manual_clock"],"id":109}],[{"start":{"row":21,"column":1},"end":{"row":21,"column":2},"action":"insert","lines":[" "],"id":110}],[{"start":{"row":21,"column":2},"end":{"row":21,"column":19},"action":"insert","lines":["edit_manual_clock"],"id":111}],[{"start":{"row":20,"column":87},"end":{"row":21,"column":0},"action":"insert","lines":["",""],"id":112},{"start":{"row":21,"column":0},"end":{"row":21,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":21,"column":4},"end":{"row":21,"column":60},"action":"insert","lines":["url(r'^(?P<pk>\\d+)/edit_fm/$', edit_fm, name='edit_fm'),"],"id":113}],[{"start":{"row":22,"column":2},"end":{"row":22,"column":19},"action":"remove","lines":["edit_manual_clock"],"id":114}],[{"start":{"row":21,"column":23},"end":{"row":21,"column":30},"action":"remove","lines":["edit_fm"],"id":115}],[{"start":{"row":21,"column":23},"end":{"row":21,"column":40},"action":"insert","lines":["edit_manual_clock"],"id":116}],[{"start":{"row":21,"column":45},"end":{"row":21,"column":52},"action":"remove","lines":["edit_fm"],"id":117}],[{"start":{"row":21,"column":45},"end":{"row":21,"column":62},"action":"insert","lines":["edit_manual_clock"],"id":118}],[{"start":{"row":21,"column":70},"end":{"row":21,"column":77},"action":"remove","lines":["edit_fm"],"id":119}],[{"start":{"row":21,"column":70},"end":{"row":21,"column":87},"action":"insert","lines":["edit_manual_clock"],"id":120}],[{"start":{"row":22,"column":2},"end":{"row":22,"column":21},"action":"insert","lines":["delete_manual_clock"],"id":121}],[{"start":{"row":1,"column":372},"end":{"row":1,"column":373},"action":"insert","lines":[","],"id":122}],[{"start":{"row":1,"column":373},"end":{"row":1,"column":374},"action":"insert","lines":[" "],"id":123}],[{"start":{"row":1,"column":374},"end":{"row":1,"column":393},"action":"insert","lines":["delete_manual_clock"],"id":124}],[{"start":{"row":21,"column":90},"end":{"row":22,"column":0},"action":"insert","lines":["",""],"id":125},{"start":{"row":22,"column":0},"end":{"row":22,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":22,"column":4},"end":{"row":22,"column":66},"action":"insert","lines":["url(r'^(?P<pk>\\d+)/delete_fm/$', delete_fm, name='delete_fm'),"],"id":126}],[{"start":{"row":23,"column":2},"end":{"row":23,"column":21},"action":"remove","lines":["delete_manual_clock"],"id":127}],[{"start":{"row":22,"column":23},"end":{"row":22,"column":32},"action":"remove","lines":["delete_fm"],"id":128}],[{"start":{"row":22,"column":23},"end":{"row":22,"column":42},"action":"insert","lines":["delete_manual_clock"],"id":129}],[{"start":{"row":22,"column":47},"end":{"row":22,"column":56},"action":"remove","lines":["delete_fm"],"id":130}],[{"start":{"row":22,"column":47},"end":{"row":22,"column":66},"action":"insert","lines":["delete_manual_clock"],"id":131}],[{"start":{"row":22,"column":74},"end":{"row":22,"column":83},"action":"remove","lines":["delete_fm"],"id":132}],[{"start":{"row":22,"column":74},"end":{"row":22,"column":93},"action":"insert","lines":["delete_manual_clock"],"id":133}],[{"start":{"row":1,"column":48},"end":{"row":1,"column":66},"action":"remove","lines":["generate_quarters,"],"id":134}],[{"start":{"row":1,"column":47},"end":{"row":1,"column":48},"action":"remove","lines":[" "],"id":135}],[{"start":{"row":6,"column":4},"end":{"row":6,"column":5},"action":"insert","lines":["#"],"id":136}],[{"start":{"row":1,"column":374},"end":{"row":1,"column":375},"action":"insert","lines":[","],"id":137}],[{"start":{"row":1,"column":375},"end":{"row":1,"column":376},"action":"insert","lines":[" "],"id":138}],[{"start":{"row":1,"column":376},"end":{"row":1,"column":396},"action":"insert","lines":["remote_clocking_page"],"id":139}],[{"start":{"row":23,"column":2},"end":{"row":23,"column":22},"action":"insert","lines":["remote_clocking_page"],"id":140}],[{"start":{"row":22,"column":96},"end":{"row":23,"column":0},"action":"insert","lines":["",""],"id":141},{"start":{"row":23,"column":0},"end":{"row":23,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":23,"column":4},"end":{"row":23,"column":102},"action":"insert","lines":["url(r'^previous_manual_clockings/$', previous_manual_clockings, name='previous_manual_clockings'),"],"id":142}],[{"start":{"row":24,"column":2},"end":{"row":24,"column":22},"action":"remove","lines":["remote_clocking_page"],"id":143}],[{"start":{"row":24,"column":1},"end":{"row":24,"column":2},"action":"remove","lines":[" "],"id":144}],[{"start":{"row":23,"column":11},"end":{"row":23,"column":36},"action":"remove","lines":["previous_manual_clockings"],"id":145},{"start":{"row":23,"column":11},"end":{"row":23,"column":31},"action":"insert","lines":["remote_clocking_page"]}],[{"start":{"row":23,"column":36},"end":{"row":23,"column":61},"action":"remove","lines":["previous_manual_clockings"],"id":146},{"start":{"row":23,"column":36},"end":{"row":23,"column":56},"action":"insert","lines":["remote_clocking_page"]}],[{"start":{"row":23,"column":64},"end":{"row":23,"column":89},"action":"remove","lines":["previous_manual_clockings"],"id":147},{"start":{"row":23,"column":64},"end":{"row":23,"column":84},"action":"insert","lines":["remote_clocking_page"]}],[{"start":{"row":23,"column":86},"end":{"row":23,"column":87},"action":"remove","lines":[","],"id":148}],[{"start":{"row":24,"column":1},"end":{"row":24,"column":2},"action":"insert","lines":[" "],"id":149}],[{"start":{"row":24,"column":2},"end":{"row":24,"column":23},"action":"insert","lines":["view_remote_clockings"],"id":150}],[{"start":{"row":1,"column":396},"end":{"row":1,"column":397},"action":"insert","lines":[","],"id":151}],[{"start":{"row":1,"column":397},"end":{"row":1,"column":398},"action":"insert","lines":[" "],"id":152}],[{"start":{"row":1,"column":398},"end":{"row":1,"column":419},"action":"insert","lines":["view_remote_clockings"],"id":153}],[{"start":{"row":23,"column":86},"end":{"row":23,"column":87},"action":"insert","lines":[","],"id":154}],[{"start":{"row":23,"column":87},"end":{"row":24,"column":0},"action":"insert","lines":["",""],"id":155},{"start":{"row":24,"column":0},"end":{"row":24,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":24,"column":4},"end":{"row":24,"column":120},"action":"insert","lines":["url(r'^view_submitted_manual_clockings/$', view_submitted_manual_clockings, name='view_submitted_manual_clockings'),"],"id":156}],[{"start":{"row":24,"column":11},"end":{"row":24,"column":42},"action":"remove","lines":["view_submitted_manual_clockings"],"id":157},{"start":{"row":24,"column":11},"end":{"row":24,"column":32},"action":"insert","lines":["view_remote_clockings"]}],[{"start":{"row":24,"column":37},"end":{"row":24,"column":68},"action":"remove","lines":["view_submitted_manual_clockings"],"id":158},{"start":{"row":24,"column":37},"end":{"row":24,"column":58},"action":"insert","lines":["view_remote_clockings"]}],[{"start":{"row":24,"column":66},"end":{"row":24,"column":97},"action":"remove","lines":["view_submitted_manual_clockings"],"id":159},{"start":{"row":24,"column":66},"end":{"row":24,"column":87},"action":"insert","lines":["view_remote_clockings"]}],[{"start":{"row":25,"column":22},"end":{"row":25,"column":23},"action":"remove","lines":["s"],"id":160},{"start":{"row":25,"column":21},"end":{"row":25,"column":22},"action":"remove","lines":["g"]},{"start":{"row":25,"column":20},"end":{"row":25,"column":21},"action":"remove","lines":["n"]},{"start":{"row":25,"column":19},"end":{"row":25,"column":20},"action":"remove","lines":["i"]},{"start":{"row":25,"column":18},"end":{"row":25,"column":19},"action":"remove","lines":["k"]},{"start":{"row":25,"column":17},"end":{"row":25,"column":18},"action":"remove","lines":["c"]},{"start":{"row":25,"column":16},"end":{"row":25,"column":17},"action":"remove","lines":["o"]},{"start":{"row":25,"column":15},"end":{"row":25,"column":16},"action":"remove","lines":["l"]},{"start":{"row":25,"column":14},"end":{"row":25,"column":15},"action":"remove","lines":["c"]},{"start":{"row":25,"column":13},"end":{"row":25,"column":14},"action":"remove","lines":["_"]},{"start":{"row":25,"column":12},"end":{"row":25,"column":13},"action":"remove","lines":["e"]},{"start":{"row":25,"column":11},"end":{"row":25,"column":12},"action":"remove","lines":["t"]},{"start":{"row":25,"column":10},"end":{"row":25,"column":11},"action":"remove","lines":["o"]},{"start":{"row":25,"column":9},"end":{"row":25,"column":10},"action":"remove","lines":["m"]},{"start":{"row":25,"column":8},"end":{"row":25,"column":9},"action":"remove","lines":["e"]},{"start":{"row":25,"column":7},"end":{"row":25,"column":8},"action":"remove","lines":["r"]},{"start":{"row":25,"column":6},"end":{"row":25,"column":7},"action":"remove","lines":["_"]},{"start":{"row":25,"column":5},"end":{"row":25,"column":6},"action":"remove","lines":["w"]},{"start":{"row":25,"column":4},"end":{"row":25,"column":5},"action":"remove","lines":["e"]},{"start":{"row":25,"column":3},"end":{"row":25,"column":4},"action":"remove","lines":["i"]},{"start":{"row":25,"column":2},"end":{"row":25,"column":3},"action":"remove","lines":["v"]},{"start":{"row":25,"column":1},"end":{"row":25,"column":2},"action":"remove","lines":[" "]}]]},"ace":{"folds":[],"scrolltop":14,"scrollleft":0,"selection":{"start":{"row":24,"column":11},"end":{"row":24,"column":32},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1617118649464,"hash":"7b2422835b05b384fe3f41787057e3d0214681b0"}