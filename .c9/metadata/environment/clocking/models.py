{"filter":false,"title":"models.py","tooltip":"/clocking/models.py","undoManager":{"mark":4,"position":4,"stack":[[{"start":{"row":1,"column":0},"end":{"row":2,"column":36},"action":"insert","lines":["from account.models import Account","from account.utils import ChoiceEnum"],"id":2}],[{"start":{"row":2,"column":36},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":3}],[{"start":{"row":5,"column":0},"end":{"row":14,"column":29},"action":"insert","lines":["class Quarter(models.Model):","    qtr_start_date = models.DateField(blank=True, null=True)","    qtr_end_date = models.DateField(blank=True, null=True)","    qtr_label = models.CharField(max_length=5, blank=False, null=False)","    ","    def __unicode__(self):","\t    return self.qtr_label","","    def __str__(self):","        return self.qtr_label"],"id":4}],[{"start":{"row":14,"column":29},"end":{"row":15,"column":0},"action":"insert","lines":["",""],"id":5},{"start":{"row":15,"column":0},"end":{"row":15,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":15,"column":4},"end":{"row":15,"column":8},"action":"remove","lines":["    "],"id":6},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"remove","lines":["    "]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":15,"column":0},"end":{"row":15,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1605551837493,"hash":"31cbfbf8bd7be5bba92aa56c86d7a9aee946862c"}