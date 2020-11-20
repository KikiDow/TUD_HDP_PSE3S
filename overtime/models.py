from django.db import models
from account.models import Account
from clocking.models import Quarter, Shift

# Create your models here.
class Overtime(models.Model):
    ot_officer_id = models.ForeignKey(Account, related_name='ot_officer_id', on_delete=models.CASCADE)
    ot_qtr_id = models.ForeignKey(Quarter, related_name='ot_qtr_id', on_delete=models.CASCADE)
    ot_date = models.DateField(blank=True, null=True)
    ot_shift_id = models.ForeignKey(Shift, related_name='ot_shift_id', on_delete=models.CASCADE)
    ot_recall = models.BooleanField(default=False)
    ot_requirement = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.ot_date
        
    def __str__(self):
        return str(self.ot_officer_id) + " has overtime on " + str(self.ot_date)
        
class ShortOvertime(models.Model):
    short_ot_officer_id = models.ForeignKey(Account, related_name='short_ot_officer_id', on_delete=models.CASCADE)
    short_ot_qtr_id = models.ForeignKey(Quarter, related_name='short_ot_qtr_id', on_delete=models.CASCADE)
    short_ot_date = models.DateField(blank=False, null=False)
    short_ot_start_time = models.TimeField(blank=False, null=False)
    short_ot_end_time = models.TimeField(blank=False, null=False)
    overtime_hours = models.FloatField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.short_ot_date
        
    def __str__(self):
        return str(self.short_ot_officer_id) + " has short overtime on " + str(self.short_ot_date)
        
class OvertimePerQtr(models.Model):
    ot_per_qtr_off_id = models.ForeignKey(Account, related_name='ot_per_qtr_off_id', on_delete=models.CASCADE)
    ot_per_qtr_qtr_id = models.ForeignKey(Quarter, related_name='ot_per_qtr_qtr_id', on_delete=models.CASCADE)
    ot_hours_completed = models.FloatField(blank=False, null=False, default=0.0)
    avail_window_open = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.ot_per_qtr_qtr_id
        
    def __str__(self):
        return str(self.ot_per_qtr_off_id) + " for " + str(self.ot_per_qtr_qtr_id)
        
class AvailabilitySheet(models.Model):
    avail_sheet_off_id = models.ForeignKey(Account, related_name='avail_sheet_off_id', on_delete=models.CASCADE)
    avail_sheet_qtr_id = models.ForeignKey(Quarter, related_name='avail_sheet_qtr_id', on_delete=models.CASCADE)
    mon_one = models.DateField(blank=False, null=False)
    mon_two = models.DateField(blank=False, null=False)
    tue_one = models.DateField(blank=False, null=False)
    tue_two = models.DateField(blank=False, null=False)
    wed_one = models.DateField(blank=False, null=False)
    wed_two = models.DateField(blank=False, null=False)
    thurs_one = models.DateField(blank=False, null=False)
    thurs_two = models.DateField(blank=False, null=False)
    fri_one = models.DateField(blank=False, null=False)
    fri_two = models.DateField(blank=False, null=False)
    sat_one = models.DateField(blank=False, null=False)
    sat_two = models.DateField(blank=False, null=False)
    sun_one = models.DateField(blank=False, null=False)
    sun_two = models.DateField(blank=False, null=False)
    avail_sheet_date_submitted = models.DateField(auto_now_add=True)
    
    def __unicode__(self):
        return self.avail_sheet_qtr_id
        
    def __str__(self):
        return str(self.avail_sheet_off_id) + " avail sheet for " + str(self.avail_sheet_qtr_id)
        
class ShortTermAvailabilty(models.Model):
    st_availability_off_id = models.ForeignKey(Account, related_name='st_availability_off_id', on_delete=models.CASCADE)
    st_availability_qtr_id = models.ForeignKey(Quarter, related_name='st_availability_qtr_id', on_delete=models.CASCADE)
    st_availability_date = models.DateField(blank=False, null=False)
    
    def __unicode__(self):
        return self.st_availability_qtr_id
        
    def __str__(self):
        return str(self.st_availability_off_id) + " st available on " + str(self.st_availability_date)
        
class NonScheduledOvertimeRequest(models.Model):
    nsot_off_id = models.ForeignKey(Account, related_name='nsot_off_id', on_delete=models.CASCADE)
    nsot_date = models.DateField(blank=False, null=False)
    nsot_start_time = models.TimeField(blank=False, null=False)
    nsot_end_time = models.TimeField(blank=False, null=False)
    ot_hours_claimed = models.FloatField(blank=True, null=True)
    nsot_task = models.CharField(max_length=600, blank=False, null=False)
    directed_by = models.CharField(max_length=600, blank=False, null=False)
    nsot_date_submitted = models.DateField(auto_now_add=True)
    nsot_checked_by_validator = models.BooleanField(default=False)
    nsot_accepted = models.BooleanField(default=False)
    reason_nsot_rejected = models.CharField(max_length=600, blank=True, null=True)
    
    def __unicode__(self):
        return self.nsot_date
        
    def __str__(self):
        return str(self.nsot_off_id) + " nsot request for " + str(self.nsot_date)
        
class AllowancesRequest(models.Model):
    allow_req_off_id = models.ForeignKey(Account, related_name='allow_req_off_id', on_delete=models.CASCADE)
    allow_req_task = models.CharField(max_length=600, blank=False, null=False)
    allow_req_date = models.DateField(blank=False, null=False)
    claiming_breakfast_allowance = models.BooleanField(default=False)
    claiming_dinner_allowance = models.BooleanField(default=False)
    claiming_tea_allowance = models.BooleanField(default=False)
    claiming_plain_clothes_allowance = models.BooleanField(default=False)
    claiming_food_for_prisoner_expense = models.BooleanField(default=False)
    food_for_prisoner_amount = models.FloatField(blank=True, null=True)
    receipt_for_prisoner_food = models.ImageField(upload_to='food_receipts_images', blank=True, null=True)
    claim_total = models.FloatField(blank=True, null=True)
    allow_req_date_submitted = models.DateField(auto_now_add=True)
    allow_req_checked_by_validator = models.BooleanField(default=False)
    allow_req_accepted = models.BooleanField(default=False)
    reason_allowance_req_rejected = models.CharField(max_length=600, blank=True, null=True)
    
    def __unicode__(self):
        return self.allow_req_date
        
    def __str__(self):
        return str(self.allow_req_off_id) + " allowance request for " + str(self.allow_req_date)