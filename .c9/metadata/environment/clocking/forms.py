{"filter":false,"title":"forms.py","tooltip":"/clocking/forms.py","undoManager":{"mark":19,"position":19,"stack":[[{"start":{"row":0,"column":0},"end":{"row":1,"column":35},"action":"insert","lines":["from django import forms","from .models import PersonalDetails"],"id":1}],[{"start":{"row":1,"column":35},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":3,"column":0},"end":{"row":6,"column":89},"action":"insert","lines":["class PersonalDetailsForm(forms.ModelForm):","    class Meta:","        model = PersonalDetails","        fields = ('address_1', 'address_2', 'county', 'contact_number', 'personal_email')"],"id":3}],[{"start":{"row":6,"column":44},"end":{"row":6,"column":46},"action":"insert","lines":["''"],"id":4}],[{"start":{"row":6,"column":45},"end":{"row":6,"column":52},"action":"insert","lines":["eircode"],"id":5}],[{"start":{"row":6,"column":53},"end":{"row":6,"column":54},"action":"insert","lines":[","],"id":6}],[{"start":{"row":6,"column":54},"end":{"row":6,"column":55},"action":"insert","lines":[" "],"id":7}],[{"start":{"row":6,"column":99},"end":{"row":6,"column":100},"action":"insert","lines":[","],"id":8}],[{"start":{"row":6,"column":100},"end":{"row":6,"column":101},"action":"insert","lines":[" "],"id":9}],[{"start":{"row":6,"column":101},"end":{"row":6,"column":103},"action":"insert","lines":["''"],"id":10}],[{"start":{"row":6,"column":102},"end":{"row":6,"column":119},"action":"insert","lines":["emergency_contact"],"id":11}],[{"start":{"row":6,"column":120},"end":{"row":6,"column":121},"action":"insert","lines":[","],"id":12}],[{"start":{"row":6,"column":121},"end":{"row":6,"column":122},"action":"insert","lines":[" "],"id":13}],[{"start":{"row":6,"column":122},"end":{"row":6,"column":124},"action":"insert","lines":["''"],"id":14}],[{"start":{"row":6,"column":123},"end":{"row":6,"column":156},"action":"insert","lines":["relationship_to_emergency_contact"],"id":15}],[{"start":{"row":6,"column":157},"end":{"row":6,"column":158},"action":"insert","lines":[","],"id":16}],[{"start":{"row":6,"column":158},"end":{"row":6,"column":159},"action":"insert","lines":[" "],"id":17}],[{"start":{"row":6,"column":159},"end":{"row":6,"column":161},"action":"insert","lines":["''"],"id":18}],[{"start":{"row":6,"column":160},"end":{"row":6,"column":184},"action":"insert","lines":["emergency_contact_number"],"id":19}],[{"start":{"row":6,"column":186},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":20},{"start":{"row":7,"column":0},"end":{"row":7,"column":8},"action":"insert","lines":["        "]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":7,"column":0},"end":{"row":7,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1605695137245,"hash":"1bd2d2ff2e4feb5c27a9d32668fda12aa314a119"}