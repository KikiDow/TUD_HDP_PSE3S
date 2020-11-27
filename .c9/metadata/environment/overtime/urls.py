{"filter":false,"title":"urls.py","tooltip":"/overtime/urls.py","undoManager":{"mark":65,"position":65,"stack":[[{"start":{"row":1,"column":379},"end":{"row":1,"column":380},"action":"insert","lines":[","],"id":79}],[{"start":{"row":1,"column":380},"end":{"row":1,"column":381},"action":"insert","lines":[" "],"id":80}],[{"start":{"row":1,"column":381},"end":{"row":1,"column":400},"action":"insert","lines":["accept_nsot_request"],"id":81}],[{"start":{"row":18,"column":99},"end":{"row":19,"column":0},"action":"insert","lines":["",""],"id":82},{"start":{"row":19,"column":0},"end":{"row":19,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":19,"column":4},"end":{"row":19,"column":96},"action":"insert","lines":["url(r'^(?P<pk>\\d+)/accept_nsot_request/$', accept_nsot_request, name='accept_nsot_request'),"],"id":83}],[{"start":{"row":1,"column":400},"end":{"row":1,"column":401},"action":"insert","lines":[","],"id":84}],[{"start":{"row":1,"column":401},"end":{"row":1,"column":402},"action":"insert","lines":[" "],"id":85}],[{"start":{"row":1,"column":402},"end":{"row":1,"column":421},"action":"insert","lines":["reject_nsot_request"],"id":86}],[{"start":{"row":19,"column":96},"end":{"row":20,"column":0},"action":"insert","lines":["",""],"id":87},{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":20,"column":4},"end":{"row":20,"column":97},"action":"insert","lines":[" url(r'^(?P<pk>\\d+)/reject_nsot_request/$', reject_nsot_request, name='reject_nsot_request'),"],"id":88}],[{"start":{"row":20,"column":4},"end":{"row":20,"column":5},"action":"remove","lines":[" "],"id":89}],[{"start":{"row":1,"column":421},"end":{"row":1,"column":422},"action":"insert","lines":[","],"id":90}],[{"start":{"row":1,"column":422},"end":{"row":1,"column":423},"action":"insert","lines":[" "],"id":91}],[{"start":{"row":1,"column":423},"end":{"row":1,"column":440},"action":"insert","lines":["availability_page"],"id":92}],[{"start":{"row":20,"column":96},"end":{"row":21,"column":0},"action":"insert","lines":["",""],"id":93},{"start":{"row":21,"column":0},"end":{"row":21,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":21,"column":4},"end":{"row":21,"column":78},"action":"insert","lines":["url(r'^availability_page/$', availability_page, name='availability_page'),"],"id":94}],[{"start":{"row":1,"column":440},"end":{"row":1,"column":441},"action":"insert","lines":[","],"id":95}],[{"start":{"row":1,"column":441},"end":{"row":1,"column":442},"action":"insert","lines":[" "],"id":96}],[{"start":{"row":1,"column":442},"end":{"row":1,"column":467},"action":"insert","lines":["submit_availability_sheet"],"id":97}],[{"start":{"row":21,"column":78},"end":{"row":22,"column":0},"action":"insert","lines":["",""],"id":98},{"start":{"row":22,"column":0},"end":{"row":22,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":22,"column":4},"end":{"row":22,"column":102},"action":"insert","lines":["url(r'^submit_availability_sheet/$', submit_availability_sheet, name='submit_availability_sheet'),"],"id":99}],[{"start":{"row":1,"column":467},"end":{"row":1,"column":468},"action":"insert","lines":[","],"id":100}],[{"start":{"row":1,"column":468},"end":{"row":1,"column":469},"action":"insert","lines":[" "],"id":101}],[{"start":{"row":1,"column":469},"end":{"row":1,"column":492},"action":"insert","lines":["view_availability_sheet"],"id":102}],[{"start":{"row":22,"column":102},"end":{"row":23,"column":0},"action":"insert","lines":["",""],"id":103},{"start":{"row":23,"column":0},"end":{"row":23,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":23,"column":4},"end":{"row":23,"column":107},"action":"insert","lines":["url(r'^(?P<pk>\\d+)view_availability_sheet/$', view_availability_sheet, name='view_availability_sheet'),"],"id":104}],[{"start":{"row":1,"column":492},"end":{"row":1,"column":493},"action":"insert","lines":[","],"id":105}],[{"start":{"row":1,"column":493},"end":{"row":1,"column":494},"action":"insert","lines":[" "],"id":106}],[{"start":{"row":1,"column":494},"end":{"row":1,"column":519},"action":"insert","lines":["delete_availability_sheet"],"id":107}],[{"start":{"row":23,"column":107},"end":{"row":24,"column":0},"action":"insert","lines":["",""],"id":108},{"start":{"row":24,"column":0},"end":{"row":24,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":24,"column":4},"end":{"row":24,"column":114},"action":"insert","lines":["url(r'^(?P<pk>\\d+)/delete_availability_sheet/$', delete_availability_sheet, name='delete_availability_sheet'),"],"id":109}],[{"start":{"row":1,"column":519},"end":{"row":1,"column":520},"action":"insert","lines":[","],"id":110}],[{"start":{"row":1,"column":520},"end":{"row":1,"column":521},"action":"insert","lines":[" "],"id":111}],[{"start":{"row":1,"column":521},"end":{"row":1,"column":535},"action":"insert","lines":["assign_ot_date"],"id":112}],[{"start":{"row":24,"column":114},"end":{"row":25,"column":0},"action":"insert","lines":["",""],"id":113},{"start":{"row":25,"column":0},"end":{"row":25,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":25,"column":4},"end":{"row":25,"column":69},"action":"insert","lines":["url(r'^assign_ot_date/$', assign_ot_date, name='assign_ot_date'),"],"id":114}],[{"start":{"row":25,"column":69},"end":{"row":26,"column":0},"action":"insert","lines":["",""],"id":115},{"start":{"row":26,"column":0},"end":{"row":26,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":26,"column":4},"end":{"row":26,"column":110},"action":"insert","lines":["url(r'^(?P<chosen_date>\\d{4}-\\d{2}-\\d{2})/assign_ot_recall/$', assign_ot_recall, name='assign_ot_recall'),"],"id":116}],[{"start":{"row":1,"column":535},"end":{"row":1,"column":536},"action":"insert","lines":[","],"id":117}],[{"start":{"row":1,"column":536},"end":{"row":1,"column":537},"action":"insert","lines":[" "],"id":118}],[{"start":{"row":1,"column":537},"end":{"row":1,"column":553},"action":"insert","lines":["assign_ot_recall"],"id":119}],[{"start":{"row":1,"column":553},"end":{"row":1,"column":554},"action":"insert","lines":[","],"id":120}],[{"start":{"row":1,"column":554},"end":{"row":1,"column":555},"action":"insert","lines":[" "],"id":121}],[{"start":{"row":1,"column":555},"end":{"row":1,"column":572},"action":"insert","lines":["assign_ot_require"],"id":122}],[{"start":{"row":26,"column":110},"end":{"row":27,"column":0},"action":"insert","lines":["",""],"id":123},{"start":{"row":27,"column":0},"end":{"row":27,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":27,"column":4},"end":{"row":27,"column":115},"action":"insert","lines":["url(r'^(?P<date_selected>\\d{4}-\\d{2}-\\d{2})/assign_ot_require/$', assign_ot_require, name='assign_ot_require'),"],"id":124}],[{"start":{"row":1,"column":572},"end":{"row":1,"column":573},"action":"insert","lines":[","],"id":125}],[{"start":{"row":1,"column":573},"end":{"row":1,"column":574},"action":"insert","lines":[" "],"id":126}],[{"start":{"row":1,"column":574},"end":{"row":1,"column":591},"action":"insert","lines":["search_allowances"],"id":127}],[{"start":{"row":28,"column":1},"end":{"row":28,"column":18},"action":"insert","lines":["search_allowances"],"id":128}],[{"start":{"row":27,"column":115},"end":{"row":28,"column":0},"action":"insert","lines":["",""],"id":129},{"start":{"row":28,"column":0},"end":{"row":28,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":28,"column":4},"end":{"row":28,"column":69},"action":"insert","lines":["url(r'^assign_ot_date/$', assign_ot_date, name='assign_ot_date'),"],"id":130}],[{"start":{"row":29,"column":1},"end":{"row":29,"column":18},"action":"remove","lines":["search_allowances"],"id":131}],[{"start":{"row":28,"column":11},"end":{"row":28,"column":25},"action":"remove","lines":["assign_ot_date"],"id":132},{"start":{"row":28,"column":11},"end":{"row":28,"column":28},"action":"insert","lines":["search_allowances"]}],[{"start":{"row":28,"column":33},"end":{"row":28,"column":47},"action":"remove","lines":["assign_ot_date"],"id":133},{"start":{"row":28,"column":33},"end":{"row":28,"column":50},"action":"insert","lines":["search_allowances"]}],[{"start":{"row":28,"column":58},"end":{"row":28,"column":72},"action":"remove","lines":["assign_ot_date"],"id":134},{"start":{"row":28,"column":58},"end":{"row":28,"column":75},"action":"insert","lines":["search_allowances"]}],[{"start":{"row":1,"column":591},"end":{"row":1,"column":592},"action":"insert","lines":[","],"id":135}],[{"start":{"row":1,"column":592},"end":{"row":1,"column":593},"action":"insert","lines":[" "],"id":136}],[{"start":{"row":1,"column":593},"end":{"row":1,"column":604},"action":"insert","lines":["search_nsot"],"id":137}],[{"start":{"row":29,"column":1},"end":{"row":29,"column":12},"action":"insert","lines":["search_nsot"],"id":138}],[{"start":{"row":28,"column":78},"end":{"row":29,"column":0},"action":"insert","lines":["",""],"id":139},{"start":{"row":29,"column":0},"end":{"row":29,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":29,"column":4},"end":{"row":29,"column":78},"action":"insert","lines":["url(r'^search_allowances/$', search_allowances, name='search_allowances'),"],"id":140}],[{"start":{"row":30,"column":1},"end":{"row":30,"column":12},"action":"remove","lines":["search_nsot"],"id":141}],[{"start":{"row":29,"column":11},"end":{"row":29,"column":28},"action":"remove","lines":["search_allowances"],"id":142},{"start":{"row":29,"column":11},"end":{"row":29,"column":22},"action":"insert","lines":["search_nsot"]}],[{"start":{"row":29,"column":27},"end":{"row":29,"column":44},"action":"remove","lines":["search_allowances"],"id":143},{"start":{"row":29,"column":27},"end":{"row":29,"column":38},"action":"insert","lines":["search_nsot"]}],[{"start":{"row":29,"column":46},"end":{"row":29,"column":63},"action":"remove","lines":["search_allowances"],"id":144},{"start":{"row":29,"column":46},"end":{"row":29,"column":57},"action":"insert","lines":["search_nsot"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":29,"column":11},"end":{"row":29,"column":22},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":7,"state":"start","mode":"ace/mode/python"}},"timestamp":1606491072610,"hash":"2ad957e9b3d56d8db9e11c0329f666ee3eac8df5"}