{"filter":false,"title":"custom_tags.py","tooltip":"/overtime/templatetags/custom_tags.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":7,"column":47},"action":"insert","lines":["from django import template","from django.urls import reverse","","register = template.Library()","","@register.simple_tag","def anchor(url_name, section_id):","    return reverse(url_name) + '#' + section_id"],"id":1}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":7,"column":47},"end":{"row":7,"column":47},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1607186814196,"hash":"672b3969ad157399916224ecc6c6f632b1bbbdc7"}