{"filter":false,"title":"urls.py","tooltip":"/overtime/urls.py","undoManager":{"mark":17,"position":17,"stack":[[{"start":{"row":1,"column":232},"end":{"row":1,"column":233},"action":"insert","lines":[","],"id":51}],[{"start":{"row":1,"column":233},"end":{"row":1,"column":234},"action":"insert","lines":[" "],"id":52}],[{"start":{"row":1,"column":234},"end":{"row":1,"column":255},"action":"insert","lines":["non_scheduled_ot_page"],"id":53}],[{"start":{"row":12,"column":111},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":54},{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":13,"column":4},"end":{"row":13,"column":90},"action":"insert","lines":["url(r'^non_scheduled_ot_page/$', non_scheduled_ot_page, name='non_scheduled_ot_page'),"],"id":55}],[{"start":{"row":1,"column":255},"end":{"row":1,"column":256},"action":"insert","lines":[","],"id":56}],[{"start":{"row":1,"column":256},"end":{"row":1,"column":257},"action":"insert","lines":[" "],"id":57}],[{"start":{"row":1,"column":257},"end":{"row":1,"column":276},"action":"insert","lines":["submit_nsot_request"],"id":58}],[{"start":{"row":1,"column":276},"end":{"row":1,"column":277},"action":"insert","lines":[","],"id":59}],[{"start":{"row":1,"column":277},"end":{"row":1,"column":278},"action":"insert","lines":[" "],"id":60}],[{"start":{"row":1,"column":278},"end":{"row":1,"column":313},"action":"insert","lines":["view_non_scheduled_overtime_request"],"id":61}],[{"start":{"row":13,"column":90},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":62},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":14,"column":4},"end":{"row":15,"column":143},"action":"insert","lines":["url(r'^submit_nsot_request/$', submit_nsot_request, name='submit_nsot_request'),","    url(r'^(?P<pk>\\d+)view_non_scheduled_overtime_request/$', view_non_scheduled_overtime_request, name='view_non_scheduled_overtime_request'),"],"id":63}],[{"start":{"row":1,"column":313},"end":{"row":1,"column":314},"action":"insert","lines":[","],"id":64}],[{"start":{"row":1,"column":314},"end":{"row":1,"column":315},"action":"insert","lines":[" "],"id":65}],[{"start":{"row":1,"column":315},"end":{"row":1,"column":334},"action":"insert","lines":["delete_nsot_request"],"id":66}],[{"start":{"row":15,"column":143},"end":{"row":16,"column":0},"action":"insert","lines":["",""],"id":67},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":16,"column":4},"end":{"row":16,"column":96},"action":"insert","lines":["url(r'^(?P<pk>\\d+)/delete_nsot_request/$', delete_nsot_request, name='delete_nsot_request'),"],"id":68}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":16,"column":96},"end":{"row":16,"column":96},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":73,"mode":"ace/mode/python"}},"timestamp":1605884602577,"hash":"6d1dad0752baa4fe755b5ba20d09e9638f3074c9"}