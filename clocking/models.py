from django.db import models
from account.models import Account
from account.utils import ChoiceEnum

# Create your models here.
class Quarter(models.Model):
    qtr_start_date = models.DateField(blank=True, null=True)
    qtr_end_date = models.DateField(blank=True, null=True)
    qtr_label = models.CharField(max_length=5, blank=False, null=False)
    
    def __unicode__(self):
	    return self.qtr_label

    def __str__(self):
        return self.qtr_label
