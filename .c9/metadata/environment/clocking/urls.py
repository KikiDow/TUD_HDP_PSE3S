{"filter":false,"title":"urls.py","tooltip":"/clocking/urls.py","undoManager":{"mark":21,"position":21,"stack":[[{"start":{"row":0,"column":0},"end":{"row":1,"column":31},"action":"insert","lines":["from django.conf.urls import url, include","from .views import landing_page"],"id":1}],[{"start":{"row":1,"column":31},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":3,"column":0},"end":{"row":4,"column":43},"action":"insert","lines":["urlpatterns = [","    url(r'^$', landing_page, name='index'),"],"id":3}],[{"start":{"row":4,"column":43},"end":{"row":5,"column":0},"action":"insert","lines":["",""],"id":4},{"start":{"row":5,"column":0},"end":{"row":5,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":5,"column":0},"end":{"row":5,"column":4},"action":"remove","lines":["    "],"id":5}],[{"start":{"row":5,"column":0},"end":{"row":5,"column":1},"action":"insert","lines":["]"],"id":6}],[{"start":{"row":4,"column":43},"end":{"row":5,"column":0},"action":"insert","lines":["",""],"id":7},{"start":{"row":5,"column":0},"end":{"row":5,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":5,"column":4},"end":{"row":5,"column":78},"action":"insert","lines":["url(r'^generate_quarters/$', generate_quarters, name='generate_quarters'),"],"id":8}],[{"start":{"row":1,"column":31},"end":{"row":1,"column":32},"action":"insert","lines":[","],"id":9}],[{"start":{"row":1,"column":32},"end":{"row":1,"column":33},"action":"insert","lines":[" "],"id":10},{"start":{"row":1,"column":33},"end":{"row":1,"column":34},"action":"insert","lines":["g"]},{"start":{"row":1,"column":34},"end":{"row":1,"column":35},"action":"insert","lines":["e"]}],[{"start":{"row":1,"column":33},"end":{"row":1,"column":35},"action":"remove","lines":["ge"],"id":11},{"start":{"row":1,"column":33},"end":{"row":1,"column":52},"action":"insert","lines":["generate_quarters()"]}],[{"start":{"row":1,"column":51},"end":{"row":1,"column":52},"action":"remove","lines":[")"],"id":12},{"start":{"row":1,"column":50},"end":{"row":1,"column":51},"action":"remove","lines":["("]}],[{"start":{"row":1,"column":50},"end":{"row":1,"column":51},"action":"insert","lines":[","],"id":13}],[{"start":{"row":1,"column":51},"end":{"row":1,"column":52},"action":"insert","lines":[" "],"id":14}],[{"start":{"row":1,"column":52},"end":{"row":1,"column":65},"action":"insert","lines":["clocking_page"],"id":15}],[{"start":{"row":4,"column":43},"end":{"row":5,"column":0},"action":"insert","lines":["",""],"id":16},{"start":{"row":5,"column":0},"end":{"row":5,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":5,"column":4},"end":{"row":5,"column":66},"action":"insert","lines":["url(r'^clocking_page/$', clocking_page, name='clocking_page'),"],"id":17}],[{"start":{"row":1,"column":52},"end":{"row":1,"column":65},"action":"remove","lines":["clocking_page"],"id":18}],[{"start":{"row":1,"column":51},"end":{"row":1,"column":52},"action":"remove","lines":[" "],"id":19},{"start":{"row":1,"column":50},"end":{"row":1,"column":51},"action":"remove","lines":[","]}],[{"start":{"row":1,"column":33},"end":{"row":1,"column":46},"action":"insert","lines":["clocking_page"],"id":20}],[{"start":{"row":1,"column":46},"end":{"row":1,"column":47},"action":"insert","lines":[","],"id":21}],[{"start":{"row":1,"column":47},"end":{"row":1,"column":48},"action":"insert","lines":[" "],"id":22}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":1,"column":48},"end":{"row":1,"column":48},"isBackwards":true},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1605552738785,"hash":"d8e92c206150da0f31dfb163fda6b73e5fb9565b"}