from django.db import models
from account.models import Account
from clocking.models import Shift

# Create your models here.
class Post(models.Model):
    postee_id = models.ForeignKey(Account, related_name='postee_id', on_delete=models.CASCADE)
    possible_exchange_date = models.DateField(blank=True, null=True)
    possible_exchange_shift_id = models.ForeignKey(Shift, related_name='possible_exchange_shift_id', on_delete=models.CASCADE, blank=True, null=True)
    post_content = models.CharField(max_length=600, blank=True, null=True)
    likes = models.IntegerField(default=0)
    post_led_to_exchange = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.possible_exchange_date
        
    def __str__(self):
        return str(self.postee_id) + " wants to exchange  " + str(self.possible_exchange_date)
        
class Like(models.Model):
    post_liked = models.ForeignKey(Post, related_name='post_liked', on_delete=models.CASCADE)
    post_liked_by = models.ForeignKey(Account, related_name='post_liked_by', on_delete=models.CASCADE)
    exchange_started = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.post_liked
        
    def __str__(self):
        return str(self.post_liked) + " is liked by " + str(self.post_liked_by)
        
class ExchangeRequest(models.Model):
    exchanging_req_officer = models.ForeignKey(Account, related_name='exchanging_req_officer', on_delete=models.CASCADE)
    exchange_req_date =  models.DateField(blank=False, null=False)
    exchange_req_shift_label = models.CharField(max_length=3, blank=False)
    exchanging_req_officer_notes = models.CharField(max_length=600, blank=True, null=True)
    replacing_req_officer = models.ForeignKey(Account, related_name='replacing_req_officer', on_delete=models.CASCADE)
    replacing_req_date =  models.DateField(blank=True, null=True)
    replacing_req_shift = models.CharField(max_length=3, blank=True, null=True)
    replacing_req_officer_notes = models.CharField(max_length=600, blank=True, null=True)
    eo_proceed_with_swap = models.BooleanField(default=False)
    ro_proceed_with_swap = models.BooleanField(default=False)
    swap_confirmed = models.BooleanField(default=False)
    swap_cancelled = models.BooleanField(default=False)
    reason_exchange_cancelled = models.CharField(max_length=600, blank=True, null=True)
    
    def __unicode__(self):
        return self.exchange_req_date
        
    def __str__(self):
        return str(self.exchanging_req_officer) + " is requesting exchange on " + str(self.exchange_req_date)
        
class Exchange(models.Model):
    exchanging_officer = models.ForeignKey(Account, related_name='exchanging_officer', on_delete=models.CASCADE)
    exchange_date = models.DateField(blank=False, null=False)
    exchange_shift = models.ForeignKey(Shift, related_name='exchange_shift', on_delete=models.CASCADE)
    replacing_officer = models.ForeignKey(Account, related_name='replacing_officer', on_delete=models.CASCADE)
    replacement_date = models.DateField(blank=False, null=False)
    replacement_shift = models.ForeignKey(Shift, related_name='replacement_shift', on_delete=models.CASCADE)
    
    def __unicode__(self):
        return self.exchange_date
        
    def __str__(self):
        return str(self.exchanging_officer) + " has an exchange with " + str(self.replacing_officer) + " on " + str(self.exchange_date) + " replacing on " + str(self.replacement_date)