from django.db import models
from account.models import Account

# Create your models here.
class CertifiedSickLeave(models.Model):
    csl_officer_id = models.ForeignKey(Account, related_name='csl_officer_id', on_delete=models.CASCADE)
    first_day_of_cert = models.DateField(blank=False, null=False)
    last_day_of_cert = models.DateField(blank=False, null=False)
    csl_image = models.ImageField(upload_to='csl_images', blank=False, null=False)
    date_csl_submitted = models.DateTimeField(auto_now_add=True)
    csl_checked_by_validator = models.BooleanField(default=False)
    csl_accepted = models.BooleanField(default=False)
    reason_csl_rejected = models.CharField(max_length=400, blank=True, null=True)
    
    def __unicode__(self):
        return self.first_day_of_cert
        
    def __str__(self):
        return str(self.csl_officer_id) + " : " + str(self.first_day_of_cert) + " to " + str(self.last_day_of_cert)
        
class UnCertifiedSickLeave(models.Model):
    usl_officer_id = models.ForeignKey(Account, related_name='usl_officer_id', on_delete=models.CASCADE)
    usl_date = models.DateField(blank=False, null=False)
    reason_for_usl = models.CharField(max_length=600, blank=False, null=False)
    date_usl_submitted = models.DateTimeField(auto_now_add=True)
    usl_checked_by_validator = models.BooleanField(default=False)
    usl_accepted = models.BooleanField(default=False)
    reason_usl_rejected = models.CharField(max_length=600, blank=True, null=True)
    
    def __unicode__(self):
        return self.usl_date
        
    def __str__(self):
        return str(self.usl_officer_id) + " : " + str(self.usl_date)
        
class ForceMajeure(models.Model):
    fm_officer_id = models.ForeignKey(Account, related_name='fm_officer_id', on_delete=models.CASCADE)
    fm_date = models.DateField(blank=False, null=False)
    reason_for_fm = models.CharField(max_length=600, blank=False, null=False)
    date_fm_submitted = models.DateTimeField(auto_now_add=True)
    fm_checked_by_validator = models.BooleanField(default=False)
    fm_accepted = models.BooleanField(default=False)
    reason_fm_rejected = models.CharField(max_length=600, blank=True, null=True)
    
    def __unicode__(self):
        return self.fm_date
        
    def __str__(self):
        return str(self.fm_officer_id) + " : " + str(self.fm_date)
        
class CertifiedSickPerYear(models.Model):
    yearly_csl_officer_id = models.ForeignKey(Account, related_name='yearly_csl_officer_id', on_delete=models.CASCADE)
    csl_year = models.IntegerField(blank=False, null=False)
    number_csl_for_year = models.IntegerField(blank=False, null=False)
    
    def __unicode__(self):
        return self.csl_year
        
    def __str__(self):
        return str(self.yearly_csl_officer_id) + " : " + str(self.csl_year)
        
class UnCertifiedSickPerYear(models.Model):
    yearly_usl_officer_id = models.ForeignKey(Account, related_name='yearly_usl_officer_id', on_delete=models.CASCADE)
    usl_year = models.IntegerField(blank=False, null=False)
    number_usl_for_year = models.IntegerField(blank=False, null=False)
    
    def __unicode__(self):
        return self.usl_year
        
    def __str__(self):
        return str(self.yearly_usl_officer_id) + " : " + str(self.usl_year)
        
class ForceMajeurePerYear(models.Model):
    yearly_fm_officer_id = models.ForeignKey(Account, related_name='yearly_fm_officer_id', on_delete=models.CASCADE)
    fm_year = models.IntegerField(blank=False, null=False)
    number_fm_for_year = models.IntegerField(blank=False, null=False)
    
    def __unicode__(self):
        return self.fm_year
        
    def __str__(self):
        return str(self.yearly_fm_officer_id) + " : " + str(self.fm_year)