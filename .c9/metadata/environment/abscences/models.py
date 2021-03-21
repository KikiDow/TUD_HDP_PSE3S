{"filter":false,"title":"models.py","tooltip":"/abscences/models.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":1,"column":34},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":3}],[{"start":{"row":4,"column":0},"end":{"row":18,"column":77},"action":"insert","lines":["class CertifiedSickLeave(models.Model):","    csl_officer_id = models.ForeignKey(Account, related_name='csl_officer_id', on_delete=models.CASCADE)","    first_day_of_cert = models.DateField(blank=False, null=False)","    last_day_of_cert = models.DateField(blank=False, null=False)","    csl_image = models.ImageField(upload_to='csl_images', blank=False, null=False)","    date_csl_submitted = models.DateTimeField(auto_now_add=True)","    csl_checked_by_validator = models.BooleanField(default=False)","    csl_accepted = models.BooleanField(default=False)","    reason_csl_rejected = models.CharField(max_length=400, blank=True, null=True)","    ","    def __unicode__(self):","        return self.first_day_of_cert","        ","    def __str__(self):","        return str(self.csl_officer_id) + \" : \" + str(self.first_day_of_cert)"],"id":4}],[{"start":{"row":18,"column":77},"end":{"row":18,"column":78},"action":"insert","lines":[" "],"id":5},{"start":{"row":18,"column":78},"end":{"row":18,"column":79},"action":"insert","lines":["+"]}],[{"start":{"row":18,"column":79},"end":{"row":18,"column":80},"action":"insert","lines":[" "],"id":6}],[{"start":{"row":18,"column":80},"end":{"row":18,"column":82},"action":"insert","lines":["\"\""],"id":7}],[{"start":{"row":18,"column":81},"end":{"row":18,"column":82},"action":"insert","lines":[" "],"id":8},{"start":{"row":18,"column":82},"end":{"row":18,"column":83},"action":"insert","lines":["t"]},{"start":{"row":18,"column":83},"end":{"row":18,"column":84},"action":"insert","lines":["o"]}],[{"start":{"row":18,"column":84},"end":{"row":18,"column":85},"action":"insert","lines":[" "],"id":9}],[{"start":{"row":18,"column":86},"end":{"row":18,"column":87},"action":"insert","lines":[" "],"id":10},{"start":{"row":18,"column":87},"end":{"row":18,"column":88},"action":"insert","lines":["+"]}],[{"start":{"row":18,"column":88},"end":{"row":18,"column":89},"action":"insert","lines":[" "],"id":11}],[{"start":{"row":18,"column":89},"end":{"row":18,"column":90},"action":"insert","lines":["s"],"id":12},{"start":{"row":18,"column":90},"end":{"row":18,"column":91},"action":"insert","lines":["t"]},{"start":{"row":18,"column":91},"end":{"row":18,"column":92},"action":"insert","lines":["r"]}],[{"start":{"row":18,"column":92},"end":{"row":18,"column":94},"action":"insert","lines":["()"],"id":13}],[{"start":{"row":18,"column":93},"end":{"row":18,"column":94},"action":"insert","lines":["s"],"id":14},{"start":{"row":18,"column":94},"end":{"row":18,"column":95},"action":"insert","lines":["e"]},{"start":{"row":18,"column":95},"end":{"row":18,"column":96},"action":"insert","lines":["l"]},{"start":{"row":18,"column":96},"end":{"row":18,"column":97},"action":"insert","lines":["f"]},{"start":{"row":18,"column":97},"end":{"row":18,"column":98},"action":"insert","lines":["."]}],[{"start":{"row":18,"column":98},"end":{"row":18,"column":99},"action":"insert","lines":["l"],"id":15},{"start":{"row":18,"column":99},"end":{"row":18,"column":100},"action":"insert","lines":["a"]},{"start":{"row":18,"column":100},"end":{"row":18,"column":101},"action":"insert","lines":["s"]},{"start":{"row":18,"column":101},"end":{"row":18,"column":102},"action":"insert","lines":["t"]}],[{"start":{"row":18,"column":98},"end":{"row":18,"column":102},"action":"remove","lines":["last"],"id":16},{"start":{"row":18,"column":98},"end":{"row":18,"column":114},"action":"insert","lines":["last_day_of_cert"]}],[{"start":{"row":18,"column":115},"end":{"row":19,"column":0},"action":"insert","lines":["",""],"id":17},{"start":{"row":19,"column":0},"end":{"row":19,"column":8},"action":"insert","lines":["        "]},{"start":{"row":19,"column":8},"end":{"row":20,"column":0},"action":"insert","lines":["",""]},{"start":{"row":20,"column":0},"end":{"row":20,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":20,"column":4},"end":{"row":20,"column":8},"action":"remove","lines":["    "],"id":18},{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":20,"column":0},"end":{"row":33,"column":68},"action":"insert","lines":["class UnCertifiedSickLeave(models.Model):","    usl_officer_id = models.ForeignKey(Account, related_name='usl_officer_id', on_delete=models.CASCADE)","    usl_date = models.DateField(blank=False, null=False)","    reason_for_usl = models.CharField(max_length=600, blank=False, null=False)","    date_usl_submitted = models.DateTimeField(auto_now_add=True)","    usl_checked_by_validator = models.BooleanField(default=False)","    usl_accepted = models.BooleanField(default=False)","    reason_usl_rejected = models.CharField(max_length=600, blank=True, null=True)","    ","    def __unicode__(self):","        return self.usl_date","        ","    def __str__(self):","        return str(self.usl_officer_id) + \" : \" + str(self.usl_date)"],"id":19}],[{"start":{"row":33,"column":68},"end":{"row":34,"column":0},"action":"insert","lines":["",""],"id":20},{"start":{"row":34,"column":0},"end":{"row":34,"column":8},"action":"insert","lines":["        "]},{"start":{"row":34,"column":8},"end":{"row":35,"column":0},"action":"insert","lines":["",""]},{"start":{"row":35,"column":0},"end":{"row":35,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":35,"column":4},"end":{"row":35,"column":8},"action":"remove","lines":["    "],"id":21},{"start":{"row":35,"column":0},"end":{"row":35,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":35,"column":0},"end":{"row":48,"column":66},"action":"insert","lines":["class ForceMajeure(models.Model):","    fm_officer_id = models.ForeignKey(Account, related_name='fm_officer_id', on_delete=models.CASCADE)","    fm_date = models.DateField(blank=False, null=False)","    reason_for_fm = models.CharField(max_length=600, blank=False, null=False)","    date_fm_submitted = models.DateTimeField(auto_now_add=True)","    fm_checked_by_validator = models.BooleanField(default=False)","    fm_accepted = models.BooleanField(default=False)","    reason_fm_rejected = models.CharField(max_length=600, blank=True, null=True)","    ","    def __unicode__(self):","        return self.fm_date","        ","    def __str__(self):","        return str(self.fm_officer_id) + \" : \" + str(self.fm_date)"],"id":22}],[{"start":{"row":48,"column":66},"end":{"row":49,"column":0},"action":"insert","lines":["",""],"id":23},{"start":{"row":49,"column":0},"end":{"row":49,"column":8},"action":"insert","lines":["        "]},{"start":{"row":49,"column":8},"end":{"row":50,"column":0},"action":"insert","lines":["",""]},{"start":{"row":50,"column":0},"end":{"row":50,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":50,"column":4},"end":{"row":50,"column":8},"action":"remove","lines":["    "],"id":24},{"start":{"row":50,"column":0},"end":{"row":50,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":50,"column":0},"end":{"row":59,"column":75},"action":"insert","lines":["class CertifiedSickPerYear(models.Model):","    yearly_csl_officer_id = models.ForeignKey(Account, related_name='yearly_csl_officer_id', on_delete=models.CASCADE)","    csl_year = models.IntegerField(blank=False, null=False)","    number_csl_for_year = models.IntegerField(blank=False, null=False)","    ","    def __unicode__(self):","        return self.csl_year","        ","    def __str__(self):","        return str(self.yearly_csl_officer_id) + \" : \" + str(self.csl_year)"],"id":25}],[{"start":{"row":59,"column":75},"end":{"row":60,"column":0},"action":"insert","lines":["",""],"id":26},{"start":{"row":60,"column":0},"end":{"row":60,"column":8},"action":"insert","lines":["        "]},{"start":{"row":60,"column":8},"end":{"row":61,"column":0},"action":"insert","lines":["",""]},{"start":{"row":61,"column":0},"end":{"row":61,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":61,"column":4},"end":{"row":61,"column":8},"action":"remove","lines":["    "],"id":27},{"start":{"row":61,"column":0},"end":{"row":61,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":61,"column":0},"end":{"row":70,"column":75},"action":"insert","lines":["class UnCertifiedSickPerYear(models.Model):","    yearly_usl_officer_id = models.ForeignKey(Account, related_name='yearly_usl_officer_id', on_delete=models.CASCADE)","    usl_year = models.IntegerField(blank=False, null=False)","    number_usl_for_year = models.IntegerField(blank=False, null=False)","    ","    def __unicode__(self):","        return self.usl_year","        ","    def __str__(self):","        return str(self.yearly_usl_officer_id) + \" : \" + str(self.usl_year)"],"id":28}],[{"start":{"row":70,"column":75},"end":{"row":71,"column":0},"action":"insert","lines":["",""],"id":29},{"start":{"row":71,"column":0},"end":{"row":71,"column":8},"action":"insert","lines":["        "]},{"start":{"row":71,"column":8},"end":{"row":72,"column":0},"action":"insert","lines":["",""]},{"start":{"row":72,"column":0},"end":{"row":72,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":72,"column":4},"end":{"row":72,"column":8},"action":"remove","lines":["    "],"id":30},{"start":{"row":72,"column":0},"end":{"row":72,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":72,"column":0},"end":{"row":81,"column":73},"action":"insert","lines":["class ForceMajeurePerYear(models.Model):","    yearly_fm_officer_id = models.ForeignKey(Account, related_name='yearly_fm_officer_id', on_delete=models.CASCADE)","    fm_year = models.IntegerField(blank=False, null=False)","    number_fm_for_year = models.IntegerField(blank=False, null=False)","    ","    def __unicode__(self):","        return self.fm_year","        ","    def __str__(self):","        return str(self.yearly_fm_officer_id) + \" : \" + str(self.fm_year)"],"id":31}],[{"start":{"row":33,"column":44},"end":{"row":33,"column":45},"action":"remove","lines":[":"],"id":32}],[{"start":{"row":33,"column":44},"end":{"row":33,"column":45},"action":"insert","lines":["t"],"id":33},{"start":{"row":33,"column":45},"end":{"row":33,"column":46},"action":"insert","lines":["a"]},{"start":{"row":33,"column":46},"end":{"row":33,"column":47},"action":"insert","lines":["k"]},{"start":{"row":33,"column":47},"end":{"row":33,"column":48},"action":"insert","lines":["e"]},{"start":{"row":33,"column":48},"end":{"row":33,"column":49},"action":"insert","lines":["n"]}],[{"start":{"row":33,"column":49},"end":{"row":33,"column":50},"action":"insert","lines":[" "],"id":34},{"start":{"row":33,"column":50},"end":{"row":33,"column":51},"action":"insert","lines":["u"]},{"start":{"row":33,"column":51},"end":{"row":33,"column":52},"action":"insert","lines":["s"]},{"start":{"row":33,"column":52},"end":{"row":33,"column":53},"action":"insert","lines":["l"]}],[{"start":{"row":33,"column":53},"end":{"row":33,"column":54},"action":"insert","lines":[" "],"id":35},{"start":{"row":33,"column":54},"end":{"row":33,"column":55},"action":"insert","lines":["o"]},{"start":{"row":33,"column":55},"end":{"row":33,"column":56},"action":"insert","lines":["n"]}],[{"start":{"row":33,"column":52},"end":{"row":33,"column":53},"action":"remove","lines":["l"],"id":36},{"start":{"row":33,"column":51},"end":{"row":33,"column":52},"action":"remove","lines":["s"]},{"start":{"row":33,"column":50},"end":{"row":33,"column":51},"action":"remove","lines":["u"]}],[{"start":{"row":33,"column":50},"end":{"row":33,"column":51},"action":"insert","lines":["U"],"id":37},{"start":{"row":33,"column":51},"end":{"row":33,"column":52},"action":"insert","lines":["."]},{"start":{"row":33,"column":52},"end":{"row":33,"column":53},"action":"insert","lines":["S"]}],[{"start":{"row":33,"column":53},"end":{"row":33,"column":54},"action":"insert","lines":["."],"id":38},{"start":{"row":33,"column":54},"end":{"row":33,"column":55},"action":"insert","lines":["L"]},{"start":{"row":33,"column":55},"end":{"row":33,"column":56},"action":"insert","lines":["."]}],[{"start":{"row":48,"column":43},"end":{"row":48,"column":44},"action":"remove","lines":[":"],"id":39}],[{"start":{"row":48,"column":43},"end":{"row":48,"column":44},"action":"insert","lines":["t"],"id":40},{"start":{"row":48,"column":44},"end":{"row":48,"column":45},"action":"insert","lines":["o"]},{"start":{"row":48,"column":45},"end":{"row":48,"column":46},"action":"insert","lines":["o"]},{"start":{"row":48,"column":46},"end":{"row":48,"column":47},"action":"insert","lines":["k"]}],[{"start":{"row":48,"column":47},"end":{"row":48,"column":48},"action":"insert","lines":[" "],"id":41},{"start":{"row":48,"column":48},"end":{"row":48,"column":49},"action":"insert","lines":["F"]}],[{"start":{"row":48,"column":49},"end":{"row":48,"column":50},"action":"insert","lines":["."],"id":42},{"start":{"row":48,"column":50},"end":{"row":48,"column":51},"action":"insert","lines":["M"]},{"start":{"row":48,"column":51},"end":{"row":48,"column":52},"action":"insert","lines":["."]}],[{"start":{"row":48,"column":52},"end":{"row":48,"column":53},"action":"insert","lines":[" "],"id":43},{"start":{"row":48,"column":53},"end":{"row":48,"column":54},"action":"insert","lines":["o"]},{"start":{"row":48,"column":54},"end":{"row":48,"column":55},"action":"insert","lines":["n"]}],[{"start":{"row":59,"column":51},"end":{"row":59,"column":52},"action":"remove","lines":[":"],"id":44}],[{"start":{"row":59,"column":51},"end":{"row":59,"column":52},"action":"insert","lines":["h"],"id":45},{"start":{"row":59,"column":52},"end":{"row":59,"column":53},"action":"insert","lines":["a"]},{"start":{"row":59,"column":53},"end":{"row":59,"column":54},"action":"insert","lines":["s"]}],[{"start":{"row":59,"column":54},"end":{"row":59,"column":55},"action":"insert","lines":[" "],"id":46},{"start":{"row":59,"column":55},"end":{"row":59,"column":56},"action":"insert","lines":["t"]},{"start":{"row":59,"column":56},"end":{"row":59,"column":57},"action":"insert","lines":["a"]},{"start":{"row":59,"column":57},"end":{"row":59,"column":58},"action":"insert","lines":["k"]},{"start":{"row":59,"column":58},"end":{"row":59,"column":59},"action":"insert","lines":["e"]},{"start":{"row":59,"column":59},"end":{"row":59,"column":60},"action":"insert","lines":["n"]}],[{"start":{"row":59,"column":63},"end":{"row":59,"column":64},"action":"insert","lines":["+"],"id":47}],[{"start":{"row":59,"column":64},"end":{"row":59,"column":65},"action":"insert","lines":[" "],"id":48},{"start":{"row":59,"column":65},"end":{"row":59,"column":66},"action":"insert","lines":["s"]},{"start":{"row":59,"column":66},"end":{"row":59,"column":67},"action":"insert","lines":["t"]},{"start":{"row":59,"column":67},"end":{"row":59,"column":68},"action":"insert","lines":["r"]}],[{"start":{"row":59,"column":68},"end":{"row":59,"column":69},"action":"insert","lines":["("],"id":49},{"start":{"row":59,"column":69},"end":{"row":59,"column":70},"action":"insert","lines":["s"]},{"start":{"row":59,"column":70},"end":{"row":59,"column":71},"action":"insert","lines":["e"]},{"start":{"row":59,"column":71},"end":{"row":59,"column":72},"action":"insert","lines":["l"]},{"start":{"row":59,"column":72},"end":{"row":59,"column":73},"action":"insert","lines":["f"]},{"start":{"row":59,"column":73},"end":{"row":59,"column":74},"action":"insert","lines":["."]}],[{"start":{"row":59,"column":74},"end":{"row":59,"column":75},"action":"insert","lines":["n"],"id":50},{"start":{"row":59,"column":75},"end":{"row":59,"column":76},"action":"insert","lines":["u"]},{"start":{"row":59,"column":76},"end":{"row":59,"column":77},"action":"insert","lines":["m"]},{"start":{"row":59,"column":77},"end":{"row":59,"column":78},"action":"insert","lines":["b"]},{"start":{"row":59,"column":78},"end":{"row":59,"column":79},"action":"insert","lines":["e"]},{"start":{"row":59,"column":79},"end":{"row":59,"column":80},"action":"insert","lines":["r"]}],[{"start":{"row":59,"column":74},"end":{"row":59,"column":80},"action":"remove","lines":["number"],"id":51},{"start":{"row":59,"column":74},"end":{"row":59,"column":93},"action":"insert","lines":["number_csl_for_year"]}],[{"start":{"row":59,"column":93},"end":{"row":59,"column":94},"action":"insert","lines":[")"],"id":52}],[{"start":{"row":59,"column":94},"end":{"row":59,"column":95},"action":"insert","lines":[" "],"id":53}],[{"start":{"row":59,"column":95},"end":{"row":59,"column":96},"action":"insert","lines":["+"],"id":54}],[{"start":{"row":59,"column":96},"end":{"row":59,"column":97},"action":"insert","lines":[" "],"id":55},{"start":{"row":59,"column":97},"end":{"row":59,"column":98},"action":"insert","lines":["\""]}],[{"start":{"row":59,"column":98},"end":{"row":59,"column":99},"action":"insert","lines":[" "],"id":56},{"start":{"row":59,"column":99},"end":{"row":59,"column":100},"action":"insert","lines":["c"]},{"start":{"row":59,"column":100},"end":{"row":59,"column":101},"action":"insert","lines":["e"]},{"start":{"row":59,"column":101},"end":{"row":59,"column":102},"action":"insert","lines":["r"]},{"start":{"row":59,"column":102},"end":{"row":59,"column":103},"action":"insert","lines":["t"]},{"start":{"row":59,"column":103},"end":{"row":59,"column":104},"action":"insert","lines":["i"]},{"start":{"row":59,"column":104},"end":{"row":59,"column":105},"action":"insert","lines":["f"]},{"start":{"row":59,"column":105},"end":{"row":59,"column":106},"action":"insert","lines":["i"]},{"start":{"row":59,"column":106},"end":{"row":59,"column":107},"action":"insert","lines":["e"]},{"start":{"row":59,"column":107},"end":{"row":59,"column":108},"action":"insert","lines":["d"]}],[{"start":{"row":59,"column":108},"end":{"row":59,"column":109},"action":"insert","lines":[" "],"id":57}],[{"start":{"row":59,"column":109},"end":{"row":59,"column":110},"action":"insert","lines":["s"],"id":58},{"start":{"row":59,"column":110},"end":{"row":59,"column":111},"action":"insert","lines":["i"]},{"start":{"row":59,"column":111},"end":{"row":59,"column":112},"action":"insert","lines":["c"]},{"start":{"row":59,"column":112},"end":{"row":59,"column":113},"action":"insert","lines":["k"]}],[{"start":{"row":59,"column":113},"end":{"row":59,"column":114},"action":"insert","lines":[" "],"id":59},{"start":{"row":59,"column":114},"end":{"row":59,"column":115},"action":"insert","lines":["d"]},{"start":{"row":59,"column":115},"end":{"row":59,"column":116},"action":"insert","lines":["a"]},{"start":{"row":59,"column":116},"end":{"row":59,"column":117},"action":"insert","lines":["y"]},{"start":{"row":59,"column":117},"end":{"row":59,"column":118},"action":"insert","lines":["s"]}],[{"start":{"row":59,"column":118},"end":{"row":59,"column":119},"action":"insert","lines":[" "],"id":60},{"start":{"row":59,"column":119},"end":{"row":59,"column":120},"action":"insert","lines":["i"]},{"start":{"row":59,"column":120},"end":{"row":59,"column":121},"action":"insert","lines":["n"]}],[{"start":{"row":59,"column":121},"end":{"row":59,"column":122},"action":"insert","lines":[" "],"id":61},{"start":{"row":59,"column":122},"end":{"row":59,"column":123},"action":"insert","lines":["\""]}],[{"start":{"row":59,"column":123},"end":{"row":59,"column":124},"action":"insert","lines":[" "],"id":62}],[{"start":{"row":70,"column":51},"end":{"row":70,"column":52},"action":"remove","lines":[":"],"id":63}],[{"start":{"row":70,"column":51},"end":{"row":70,"column":52},"action":"insert","lines":["h"],"id":64},{"start":{"row":70,"column":52},"end":{"row":70,"column":53},"action":"insert","lines":["a"]},{"start":{"row":70,"column":53},"end":{"row":70,"column":54},"action":"insert","lines":["s"]}],[{"start":{"row":70,"column":54},"end":{"row":70,"column":55},"action":"insert","lines":[" "],"id":65},{"start":{"row":70,"column":55},"end":{"row":70,"column":56},"action":"insert","lines":["t"]},{"start":{"row":70,"column":56},"end":{"row":70,"column":57},"action":"insert","lines":["a"]},{"start":{"row":70,"column":57},"end":{"row":70,"column":58},"action":"insert","lines":["k"]},{"start":{"row":70,"column":58},"end":{"row":70,"column":59},"action":"insert","lines":["e"]},{"start":{"row":70,"column":59},"end":{"row":70,"column":60},"action":"insert","lines":["n"]}],[{"start":{"row":70,"column":63},"end":{"row":70,"column":64},"action":"insert","lines":["+"],"id":66},{"start":{"row":70,"column":64},"end":{"row":70,"column":65},"action":"insert","lines":["s"]},{"start":{"row":70,"column":65},"end":{"row":70,"column":66},"action":"insert","lines":["t"]},{"start":{"row":70,"column":66},"end":{"row":70,"column":67},"action":"insert","lines":["r"]},{"start":{"row":70,"column":67},"end":{"row":70,"column":68},"action":"insert","lines":["("]}],[{"start":{"row":70,"column":68},"end":{"row":70,"column":69},"action":"insert","lines":["s"],"id":67},{"start":{"row":70,"column":69},"end":{"row":70,"column":70},"action":"insert","lines":["e"]},{"start":{"row":70,"column":70},"end":{"row":70,"column":71},"action":"insert","lines":["l"]},{"start":{"row":70,"column":71},"end":{"row":70,"column":72},"action":"insert","lines":["f"]},{"start":{"row":70,"column":72},"end":{"row":70,"column":73},"action":"insert","lines":["."]},{"start":{"row":70,"column":73},"end":{"row":70,"column":74},"action":"insert","lines":["n"]}],[{"start":{"row":70,"column":74},"end":{"row":70,"column":75},"action":"insert","lines":["u"],"id":68},{"start":{"row":70,"column":75},"end":{"row":70,"column":76},"action":"insert","lines":["m"]}],[{"start":{"row":70,"column":73},"end":{"row":70,"column":76},"action":"remove","lines":["num"],"id":69},{"start":{"row":70,"column":73},"end":{"row":70,"column":92},"action":"insert","lines":["number_usl_for_year"]}],[{"start":{"row":70,"column":92},"end":{"row":70,"column":93},"action":"insert","lines":[")"],"id":70}],[{"start":{"row":70,"column":93},"end":{"row":70,"column":94},"action":"insert","lines":[" "],"id":71},{"start":{"row":70,"column":94},"end":{"row":70,"column":95},"action":"insert","lines":["+"]}],[{"start":{"row":70,"column":95},"end":{"row":70,"column":96},"action":"insert","lines":[" "],"id":72},{"start":{"row":70,"column":96},"end":{"row":70,"column":97},"action":"insert","lines":["\""]}],[{"start":{"row":70,"column":97},"end":{"row":70,"column":98},"action":"insert","lines":[" "],"id":73},{"start":{"row":70,"column":98},"end":{"row":70,"column":99},"action":"insert","lines":["u"]},{"start":{"row":70,"column":99},"end":{"row":70,"column":100},"action":"insert","lines":["n"]},{"start":{"row":70,"column":100},"end":{"row":70,"column":101},"action":"insert","lines":["d"]},{"start":{"row":70,"column":101},"end":{"row":70,"column":102},"action":"insert","lines":["c"]}],[{"start":{"row":70,"column":101},"end":{"row":70,"column":102},"action":"remove","lines":["c"],"id":74},{"start":{"row":70,"column":100},"end":{"row":70,"column":101},"action":"remove","lines":["d"]}],[{"start":{"row":70,"column":100},"end":{"row":70,"column":101},"action":"insert","lines":["c"],"id":75},{"start":{"row":70,"column":101},"end":{"row":70,"column":102},"action":"insert","lines":["e"]},{"start":{"row":70,"column":102},"end":{"row":70,"column":103},"action":"insert","lines":["r"]},{"start":{"row":70,"column":103},"end":{"row":70,"column":104},"action":"insert","lines":["t"]},{"start":{"row":70,"column":104},"end":{"row":70,"column":105},"action":"insert","lines":["i"]},{"start":{"row":70,"column":105},"end":{"row":70,"column":106},"action":"insert","lines":["f"]},{"start":{"row":70,"column":106},"end":{"row":70,"column":107},"action":"insert","lines":["i"]},{"start":{"row":70,"column":107},"end":{"row":70,"column":108},"action":"insert","lines":["e"]},{"start":{"row":70,"column":108},"end":{"row":70,"column":109},"action":"insert","lines":["d"]}],[{"start":{"row":70,"column":109},"end":{"row":70,"column":110},"action":"insert","lines":[" "],"id":76},{"start":{"row":70,"column":110},"end":{"row":70,"column":111},"action":"insert","lines":["s"]},{"start":{"row":70,"column":111},"end":{"row":70,"column":112},"action":"insert","lines":["i"]},{"start":{"row":70,"column":112},"end":{"row":70,"column":113},"action":"insert","lines":["c"]},{"start":{"row":70,"column":113},"end":{"row":70,"column":114},"action":"insert","lines":["k"]}],[{"start":{"row":70,"column":114},"end":{"row":70,"column":115},"action":"insert","lines":[" "],"id":77},{"start":{"row":70,"column":115},"end":{"row":70,"column":116},"action":"insert","lines":["d"]},{"start":{"row":70,"column":116},"end":{"row":70,"column":117},"action":"insert","lines":["a"]},{"start":{"row":70,"column":117},"end":{"row":70,"column":118},"action":"insert","lines":["y"]},{"start":{"row":70,"column":118},"end":{"row":70,"column":119},"action":"insert","lines":["s"]}],[{"start":{"row":70,"column":119},"end":{"row":70,"column":120},"action":"insert","lines":[" "],"id":78},{"start":{"row":70,"column":120},"end":{"row":70,"column":121},"action":"insert","lines":["i"]},{"start":{"row":70,"column":121},"end":{"row":70,"column":122},"action":"insert","lines":["n"]}],[{"start":{"row":70,"column":122},"end":{"row":70,"column":123},"action":"insert","lines":[" "],"id":79},{"start":{"row":70,"column":123},"end":{"row":70,"column":124},"action":"insert","lines":["\""]}],[{"start":{"row":70,"column":124},"end":{"row":70,"column":125},"action":"insert","lines":[" "],"id":80}],[{"start":{"row":70,"column":64},"end":{"row":70,"column":65},"action":"insert","lines":[" "],"id":81}],[{"start":{"row":81,"column":50},"end":{"row":81,"column":51},"action":"remove","lines":[":"],"id":82}],[{"start":{"row":81,"column":50},"end":{"row":81,"column":51},"action":"insert","lines":["h"],"id":83},{"start":{"row":81,"column":51},"end":{"row":81,"column":52},"action":"insert","lines":["a"]},{"start":{"row":81,"column":52},"end":{"row":81,"column":53},"action":"insert","lines":["s"]}],[{"start":{"row":81,"column":53},"end":{"row":81,"column":54},"action":"insert","lines":[" "],"id":84},{"start":{"row":81,"column":54},"end":{"row":81,"column":55},"action":"insert","lines":["t"]},{"start":{"row":81,"column":55},"end":{"row":81,"column":56},"action":"insert","lines":["a"]},{"start":{"row":81,"column":56},"end":{"row":81,"column":57},"action":"insert","lines":["k"]},{"start":{"row":81,"column":57},"end":{"row":81,"column":58},"action":"insert","lines":["e"]},{"start":{"row":81,"column":58},"end":{"row":81,"column":59},"action":"insert","lines":["n"]}],[{"start":{"row":81,"column":62},"end":{"row":81,"column":63},"action":"insert","lines":["+"],"id":85}],[{"start":{"row":81,"column":63},"end":{"row":81,"column":64},"action":"insert","lines":[" "],"id":86}],[{"start":{"row":81,"column":64},"end":{"row":81,"column":65},"action":"insert","lines":["s"],"id":87},{"start":{"row":81,"column":65},"end":{"row":81,"column":66},"action":"insert","lines":["t"]},{"start":{"row":81,"column":66},"end":{"row":81,"column":67},"action":"insert","lines":["r"]},{"start":{"row":81,"column":67},"end":{"row":81,"column":68},"action":"insert","lines":["("]}],[{"start":{"row":81,"column":68},"end":{"row":81,"column":69},"action":"insert","lines":["s"],"id":88},{"start":{"row":81,"column":69},"end":{"row":81,"column":70},"action":"insert","lines":["e"]},{"start":{"row":81,"column":70},"end":{"row":81,"column":71},"action":"insert","lines":["l"]},{"start":{"row":81,"column":71},"end":{"row":81,"column":72},"action":"insert","lines":["f"]},{"start":{"row":81,"column":72},"end":{"row":81,"column":73},"action":"insert","lines":["."]}],[{"start":{"row":81,"column":73},"end":{"row":81,"column":74},"action":"insert","lines":["n"],"id":89},{"start":{"row":81,"column":74},"end":{"row":81,"column":75},"action":"insert","lines":["u"]},{"start":{"row":81,"column":75},"end":{"row":81,"column":76},"action":"insert","lines":["m"]},{"start":{"row":81,"column":76},"end":{"row":81,"column":77},"action":"insert","lines":["b"]},{"start":{"row":81,"column":77},"end":{"row":81,"column":78},"action":"insert","lines":["e"]},{"start":{"row":81,"column":78},"end":{"row":81,"column":79},"action":"insert","lines":["r"]}],[{"start":{"row":81,"column":73},"end":{"row":81,"column":79},"action":"remove","lines":["number"],"id":90},{"start":{"row":81,"column":73},"end":{"row":81,"column":91},"action":"insert","lines":["number_fm_for_year"]}],[{"start":{"row":81,"column":91},"end":{"row":81,"column":92},"action":"insert","lines":[")"],"id":91}],[{"start":{"row":81,"column":92},"end":{"row":81,"column":93},"action":"insert","lines":[" "],"id":92}],[{"start":{"row":81,"column":93},"end":{"row":81,"column":94},"action":"insert","lines":["+"],"id":93}],[{"start":{"row":81,"column":94},"end":{"row":81,"column":95},"action":"insert","lines":[" "],"id":94},{"start":{"row":81,"column":95},"end":{"row":81,"column":96},"action":"insert","lines":["\""]}],[{"start":{"row":81,"column":96},"end":{"row":81,"column":97},"action":"insert","lines":[" "],"id":95},{"start":{"row":81,"column":97},"end":{"row":81,"column":98},"action":"insert","lines":["f"]},{"start":{"row":81,"column":98},"end":{"row":81,"column":99},"action":"insert","lines":["o"]},{"start":{"row":81,"column":99},"end":{"row":81,"column":100},"action":"insert","lines":["r"]},{"start":{"row":81,"column":100},"end":{"row":81,"column":101},"action":"insert","lines":["c"]},{"start":{"row":81,"column":101},"end":{"row":81,"column":102},"action":"insert","lines":["e"]}],[{"start":{"row":81,"column":102},"end":{"row":81,"column":103},"action":"insert","lines":[" "],"id":96},{"start":{"row":81,"column":103},"end":{"row":81,"column":104},"action":"insert","lines":["m"]},{"start":{"row":81,"column":104},"end":{"row":81,"column":105},"action":"insert","lines":["a"]},{"start":{"row":81,"column":105},"end":{"row":81,"column":106},"action":"insert","lines":["j"]}],[{"start":{"row":81,"column":106},"end":{"row":81,"column":107},"action":"insert","lines":["e"],"id":97},{"start":{"row":81,"column":107},"end":{"row":81,"column":108},"action":"insert","lines":["u"]},{"start":{"row":81,"column":108},"end":{"row":81,"column":109},"action":"insert","lines":["r"]},{"start":{"row":81,"column":109},"end":{"row":81,"column":110},"action":"insert","lines":["e"]}],[{"start":{"row":81,"column":110},"end":{"row":81,"column":111},"action":"insert","lines":[" "],"id":98},{"start":{"row":81,"column":111},"end":{"row":81,"column":112},"action":"insert","lines":["d"]},{"start":{"row":81,"column":112},"end":{"row":81,"column":113},"action":"insert","lines":["a"]},{"start":{"row":81,"column":113},"end":{"row":81,"column":114},"action":"insert","lines":["y"]},{"start":{"row":81,"column":114},"end":{"row":81,"column":115},"action":"insert","lines":["s"]}],[{"start":{"row":81,"column":115},"end":{"row":81,"column":116},"action":"insert","lines":[" "],"id":99},{"start":{"row":81,"column":116},"end":{"row":81,"column":117},"action":"insert","lines":["i"]},{"start":{"row":81,"column":117},"end":{"row":81,"column":118},"action":"insert","lines":["n"]}],[{"start":{"row":81,"column":118},"end":{"row":81,"column":119},"action":"insert","lines":[" "],"id":100},{"start":{"row":81,"column":119},"end":{"row":81,"column":120},"action":"insert","lines":["\""]}],[{"start":{"row":81,"column":120},"end":{"row":81,"column":121},"action":"insert","lines":[" "],"id":101}],[{"start":{"row":81,"column":140},"end":{"row":82,"column":0},"action":"insert","lines":["",""],"id":102},{"start":{"row":82,"column":0},"end":{"row":82,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":82,"column":4},"end":{"row":82,"column":8},"action":"remove","lines":["    "],"id":103},{"start":{"row":82,"column":0},"end":{"row":82,"column":4},"action":"remove","lines":["    "]},{"start":{"row":81,"column":140},"end":{"row":82,"column":0},"action":"remove","lines":["",""]}]]},"ace":{"folds":[],"scrolltop":781,"scrollleft":0,"selection":{"start":{"row":77,"column":4},"end":{"row":81,"column":140},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":153,"mode":"ace/mode/python"}},"timestamp":1605725854576,"hash":"c83b2801de5e5f3fcb36b6f66f5a7f588f9bceb1"}