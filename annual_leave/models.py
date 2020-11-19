from django.db import models
from account.models import Account

# Create your models here.
class AnnualLeaveRequest(models.Model):
    al_request_officer_id = models.ForeignKey(Account, related_name='al_request_officer_id', on_delete=models.CASCADE)
    leave_request_start_date = models.DateField(blank=True, null=True)
    leave_request_last_date = models.DateField(blank=True, null=True)
    leave_request_checked_by_validator = models.BooleanField(default=False)
    leave_request_granted = models.BooleanField(default=False)
    reason_leave_rejected = models.CharField(max_length=400, blank=True, null=True)
    
    def __unicode__(self):
        return self.al_request_officer_id
        
    def __str__(self):
        return str(self.al_request_officer_id) + " from " + str(self.leave_request_start_date) + " to " + str(self.leave_request_last_date)
    
    
class AnnualLeaveCarriedOver(models.Model):
    al_carried_over_officer_id = models.ForeignKey(Account, related_name='al_carried_over_officer_id', on_delete=models.CASCADE)
    year = models.IntegerField(blank=False, null=False)
    leave_amount_carried_over = models.IntegerField(blank=False, null=False)
    
    def __unicode__(self):
        return self.al_carried_over_officer_id
        
    def __str__(self):
        return str(self.al_carried_over_officer_id) + " - " + str(self.year)
    
class ShortTermAnnualLeaveRequest(models.Model):
    st_annual_leave_request_officer_id = models.ForeignKey(Account, related_name='st_annual_leave_request_officer_id', on_delete=models.CASCADE)
    st_leave_date = models.DateField(blank=True, null=True)
    st_leave_start_time = models.TimeField(blank=False, null=False)
    st_leave_finish_time = models.TimeField(blank=False, null=False)
    st_leave_amount = models.FloatField(blank=True, null=True)
    st_leave_request_checked_by_validator = models.BooleanField(default=False)
    st_leave_request_granted = models.BooleanField(default=False)
    reason_st_leave_rejected = models.CharField(max_length=400, blank=True, null=True)
    
    def __unicode__(self):
        return self.st_annual_leave_request_officer_id
        
    def __str__(self):
        return str(self.st_annual_leave_request_officer_id) + " - " + str(self.st_leave_date)
    
#AnnualLeave Model
class AnnualLeave(models.Model):
    al_officer_id = models.ForeignKey(Account, related_name='al_officer_id', on_delete=models.CASCADE)
    al_date = models.DateField(blank=True, null=True)
    leave_amount_used = models.IntegerField(blank=False, null=False)
    short_term_leave = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.al_officer_id
        
    def __str__(self):
        return str(self.al_officer_id) + " - " + str(self.al_date)
    
    
    