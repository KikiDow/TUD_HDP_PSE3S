{"filter":false,"title":"models.py","tooltip":"/exchanges/models.py","undoManager":{"mark":6,"position":6,"stack":[[{"start":{"row":43,"column":87},"end":{"row":44,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":44,"column":0},"end":{"row":44,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":44,"column":4},"end":{"row":44,"column":70},"action":"insert","lines":["swap_started_from_noticeboard = models.BooleanField(default=False)"],"id":3}],[{"start":{"row":37,"column":23},"end":{"row":37,"column":24},"action":"insert","lines":["_"],"id":4},{"start":{"row":37,"column":24},"end":{"row":37,"column":25},"action":"insert","lines":["l"]},{"start":{"row":37,"column":25},"end":{"row":37,"column":26},"action":"insert","lines":["a"]},{"start":{"row":37,"column":26},"end":{"row":37,"column":27},"action":"insert","lines":["b"]},{"start":{"row":37,"column":27},"end":{"row":37,"column":28},"action":"insert","lines":["e"]},{"start":{"row":37,"column":28},"end":{"row":37,"column":29},"action":"insert","lines":["l"]}],[{"start":{"row":33,"column":74},"end":{"row":34,"column":0},"action":"insert","lines":["",""],"id":5},{"start":{"row":34,"column":0},"end":{"row":34,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":34,"column":4},"end":{"row":34,"column":137},"action":"insert","lines":["exchanging_req_shift = models.ForeignKey(Shift, related_name='exchanging_req_shift', on_delete=models.CASCADE, blank=True, null=True)"],"id":6}],[{"start":{"row":38,"column":85},"end":{"row":39,"column":0},"action":"insert","lines":["",""],"id":7},{"start":{"row":39,"column":0},"end":{"row":39,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":39,"column":4},"end":{"row":39,"column":135},"action":"insert","lines":["replacing_req_shift = models.ForeignKey(Shift, related_name='replacing_req_shift', on_delete=models.CASCADE, blank=True, null=True)"],"id":8}]]},"ace":{"folds":[],"scrolltop":300,"scrollleft":0,"selection":{"start":{"row":34,"column":4},"end":{"row":34,"column":24},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":12,"state":"start","mode":"ace/mode/python"}},"timestamp":1616254211822,"hash":"ff368255342a5e07b1a73d64baece200b07ff367"}