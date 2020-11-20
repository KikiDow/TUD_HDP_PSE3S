{"filter":false,"title":"urls.py","tooltip":"/overtime/urls.py","undoManager":{"mark":49,"position":49,"stack":[[{"start":{"row":0,"column":0},"end":{"row":1,"column":32},"action":"insert","lines":["from django.conf.urls import url, include","from .views import overtime_page"],"id":1}],[{"start":{"row":1,"column":32},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"insert","lines":["",""]},{"start":{"row":3,"column":0},"end":{"row":3,"column":1},"action":"insert","lines":["u"]},{"start":{"row":3,"column":1},"end":{"row":3,"column":2},"action":"insert","lines":["r"]},{"start":{"row":3,"column":2},"end":{"row":3,"column":3},"action":"insert","lines":["l"]},{"start":{"row":3,"column":3},"end":{"row":3,"column":4},"action":"insert","lines":["p"]},{"start":{"row":3,"column":4},"end":{"row":3,"column":5},"action":"insert","lines":["a"]}],[{"start":{"row":3,"column":5},"end":{"row":3,"column":6},"action":"insert","lines":["t"],"id":3},{"start":{"row":3,"column":6},"end":{"row":3,"column":7},"action":"insert","lines":["t"]},{"start":{"row":3,"column":7},"end":{"row":3,"column":8},"action":"insert","lines":["e"]},{"start":{"row":3,"column":8},"end":{"row":3,"column":9},"action":"insert","lines":["r"]},{"start":{"row":3,"column":9},"end":{"row":3,"column":10},"action":"insert","lines":["s"]}],[{"start":{"row":3,"column":9},"end":{"row":3,"column":10},"action":"remove","lines":["s"],"id":4}],[{"start":{"row":3,"column":9},"end":{"row":3,"column":10},"action":"insert","lines":["n"],"id":5},{"start":{"row":3,"column":10},"end":{"row":3,"column":11},"action":"insert","lines":["s"]}],[{"start":{"row":3,"column":11},"end":{"row":3,"column":12},"action":"insert","lines":[" "],"id":6},{"start":{"row":3,"column":12},"end":{"row":3,"column":13},"action":"insert","lines":["="]}],[{"start":{"row":3,"column":13},"end":{"row":3,"column":15},"action":"insert","lines":["[]"],"id":7}],[{"start":{"row":3,"column":13},"end":{"row":3,"column":14},"action":"insert","lines":[" "],"id":8}],[{"start":{"row":3,"column":15},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":9},{"start":{"row":4,"column":0},"end":{"row":4,"column":4},"action":"insert","lines":["    "]},{"start":{"row":4,"column":4},"end":{"row":5,"column":0},"action":"insert","lines":["",""]},{"start":{"row":5,"column":0},"end":{"row":5,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":5,"column":0},"end":{"row":5,"column":4},"action":"remove","lines":["    "],"id":10}],[{"start":{"row":4,"column":0},"end":{"row":4,"column":4},"action":"insert","lines":["    "],"id":11}],[{"start":{"row":4,"column":4},"end":{"row":4,"column":66},"action":"insert","lines":["url(r'^overtime_page/$', overtime_page, name='overtime_page'),"],"id":12}],[{"start":{"row":1,"column":32},"end":{"row":1,"column":33},"action":"insert","lines":[","],"id":13}],[{"start":{"row":1,"column":33},"end":{"row":1,"column":34},"action":"insert","lines":[" "],"id":14}],[{"start":{"row":1,"column":34},"end":{"row":1,"column":49},"action":"insert","lines":["allowances_page"],"id":15}],[{"start":{"row":4,"column":66},"end":{"row":4,"column":70},"action":"remove","lines":["    "],"id":16},{"start":{"row":4,"column":66},"end":{"row":5,"column":0},"action":"insert","lines":["",""]},{"start":{"row":5,"column":0},"end":{"row":5,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":5,"column":4},"end":{"row":5,"column":72},"action":"insert","lines":["url(r'^allowances_page/$', allowances_page, name='allowances_page'),"],"id":17}],[{"start":{"row":1,"column":49},"end":{"row":1,"column":50},"action":"insert","lines":[","],"id":18}],[{"start":{"row":1,"column":50},"end":{"row":1,"column":51},"action":"insert","lines":[" "],"id":19}],[{"start":{"row":1,"column":51},"end":{"row":1,"column":75},"action":"insert","lines":["submit_allowance_request"],"id":20}],[{"start":{"row":5,"column":72},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":21},{"start":{"row":6,"column":0},"end":{"row":6,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":6,"column":4},"end":{"row":7,"column":104},"action":"insert","lines":["url(r'^submit_allowance_request/$', submit_allowance_request, name='submit_allowance_request'),","    url(r'^(?P<pk>\\d+)view_allowance_request/$', view_allowance_request, name='view_allowance_request'),"],"id":22}],[{"start":{"row":1,"column":75},"end":{"row":1,"column":76},"action":"insert","lines":[","],"id":23}],[{"start":{"row":1,"column":76},"end":{"row":1,"column":77},"action":"insert","lines":[" "],"id":24}],[{"start":{"row":1,"column":77},"end":{"row":1,"column":99},"action":"insert","lines":["view_allowance_request"],"id":25}],[{"start":{"row":1,"column":99},"end":{"row":1,"column":100},"action":"insert","lines":[","],"id":26}],[{"start":{"row":1,"column":100},"end":{"row":1,"column":101},"action":"insert","lines":[" "],"id":27}],[{"start":{"row":1,"column":101},"end":{"row":1,"column":123},"action":"insert","lines":["edit_allowance_request"],"id":28}],[{"start":{"row":7,"column":104},"end":{"row":8,"column":0},"action":"insert","lines":["",""],"id":29},{"start":{"row":8,"column":0},"end":{"row":8,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":8,"column":4},"end":{"row":8,"column":105},"action":"insert","lines":["url(r'^(?P<pk>\\d+)/edit_allowance_request/$', edit_allowance_request, name='edit_allowance_request'),"],"id":30}],[{"start":{"row":1,"column":123},"end":{"row":1,"column":124},"action":"insert","lines":[","],"id":31}],[{"start":{"row":1,"column":124},"end":{"row":1,"column":125},"action":"insert","lines":[" "],"id":32}],[{"start":{"row":1,"column":125},"end":{"row":1,"column":149},"action":"insert","lines":["delete_allowance_request"],"id":33}],[{"start":{"row":8,"column":105},"end":{"row":9,"column":0},"action":"insert","lines":["",""],"id":34},{"start":{"row":9,"column":0},"end":{"row":9,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":9,"column":4},"end":{"row":9,"column":111},"action":"insert","lines":["url(r'^(?P<pk>\\d+)/delete_allowance_request/$', delete_allowance_request, name='delete_allowance_request'),"],"id":35}],[{"start":{"row":1,"column":149},"end":{"row":1,"column":150},"action":"insert","lines":[","],"id":36}],[{"start":{"row":1,"column":150},"end":{"row":1,"column":151},"action":"insert","lines":[" "],"id":37}],[{"start":{"row":1,"column":151},"end":{"row":1,"column":180},"action":"insert","lines":["view_staff_allowance_requests"],"id":38}],[{"start":{"row":9,"column":111},"end":{"row":10,"column":0},"action":"insert","lines":["",""],"id":39},{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":10,"column":4},"end":{"row":10,"column":114},"action":"insert","lines":["url(r'^view_staff_allowance_requests/$', view_staff_allowance_requests, name='view_staff_allowance_requests'),"],"id":40}],[{"start":{"row":1,"column":180},"end":{"row":1,"column":181},"action":"insert","lines":[","],"id":41}],[{"start":{"row":1,"column":181},"end":{"row":1,"column":182},"action":"insert","lines":[" "],"id":42}],[{"start":{"row":1,"column":182},"end":{"row":1,"column":206},"action":"insert","lines":["accept_allowance_request"],"id":43}],[{"start":{"row":10,"column":114},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":44},{"start":{"row":11,"column":0},"end":{"row":11,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":11,"column":4},"end":{"row":11,"column":111},"action":"insert","lines":["url(r'^(?P<pk>\\d+)/accept_allowance_request/$', accept_allowance_request, name='accept_allowance_request'),"],"id":45}],[{"start":{"row":1,"column":206},"end":{"row":1,"column":207},"action":"insert","lines":[","],"id":46}],[{"start":{"row":1,"column":207},"end":{"row":1,"column":208},"action":"insert","lines":[" "],"id":47}],[{"start":{"row":1,"column":208},"end":{"row":1,"column":232},"action":"insert","lines":["reject_allowance_request"],"id":48}],[{"start":{"row":11,"column":111},"end":{"row":12,"column":0},"action":"insert","lines":["",""],"id":49},{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":12,"column":4},"end":{"row":12,"column":111},"action":"insert","lines":["url(r'^(?P<pk>\\d+)/reject_allowance_request/$', reject_allowance_request, name='reject_allowance_request'),"],"id":50}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":12,"column":111},"end":{"row":12,"column":111},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":123,"mode":"ace/mode/python"}},"timestamp":1605874006295,"hash":"ec4e6845bc3844168193c20271609483a9edf574"}