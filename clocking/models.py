from django.db import models
from account.models import Account
from account.utils import ChoiceEnum
from datetime import datetime

# Create your models here.
class Quarter(models.Model):
    qtr_start_date = models.DateField(blank=True, null=True)
    qtr_end_date = models.DateField(blank=True, null=True)
    qtr_label = models.CharField(max_length=5, blank=False, null=False)
    
    def __unicode__(self):
	    return self.qtr_label

    def __str__(self):
        return self.qtr_label

class Shift(models.Model):
    class ShiftChoices(ChoiceEnum):
    		A = 'A'
    		B = 'B'
    		C = 'C'
    shift_label = models.CharField(max_length=2,  choices=ShiftChoices.choices(), blank=False, null=False)
    shift_start_time = models.TimeField(blank=False, null=False)
    shift_end_time = models.TimeField(blank=False, null=False)
    shift_duration = models.FloatField(blank=False, null=False, default=11.0)
    
    def __unicode__(self):
        return self.shift_label
        
    def __str__(self):
        return str(self.shift_start_time) + " - " + str(self.shift_end_time)
        
class RosterSideA(models.Model):
    ros_a_shift_cycle_number = models.IntegerField(blank=False, null=False)
    ros_a_shift_label = models.CharField(max_length=3, blank=True, null=True)
    ros_a_due_on = models.BooleanField()
    
    def __unicode__(self):
        return self.ros_a_shift_cycle_number
        
    def __str__(self):
        return "Roster A Shift Cycle No: " + str(self.ros_a_shift_cycle_number)
        
class RosterSideB(models.Model):
    ros_b_shift_cycle_number = models.IntegerField(blank=False, null=False)
    ros_b_shift_label = models.CharField(max_length=3, blank=True, null=True)
    ros_b_due_on = models.BooleanField()
    
    def __unicode__(self):
        return self.ros_b_shift_cycle_number
        
    def __str__(self):
        return "Roster B Shift Cycle No: " + str(self.ros_b_shift_cycle_number)
        
class Roster(models.Model):
    roster_officer_id = models.ForeignKey(Account, related_name='roster_officer_id', on_delete=models.CASCADE)
    
    class ShiftChoices(ChoiceEnum):
    		A = 'A'
    		B = 'B'
    		C = 'C'
    		
    roster_shift_label = models.CharField(max_length=2, choices=ShiftChoices.choices(), default='None')
    roster_shift = models.ForeignKey(Shift, related_name='roster_shift', on_delete=models.CASCADE, blank=True, null=True)
    roster_shift_date = models.DateField(blank=False, null=False)
    roster_due_on = models.BooleanField()
    
    def __unicode__(self):
        return self.roster_shift_label
        
    def __str__(self):
        if self.roster_due_on == False:
            return str(self.roster_officer_id.username) + " : " + str(self.roster_shift_date) + " : " + str(self.roster_shift_label)
        else:
            return str(self.roster_officer_id.username) + " : " + str(self.roster_shift_date) + " : " + str(self.roster_shift)
            
class PersonalDetails(models.Model):
	address_1 = models.CharField(max_length=100)
	address_2 = models.CharField(max_length=100)
	eircode = models.CharField(max_length=10)
	
	class Counties(ChoiceEnum):
	    # Only limited number of counties selected to demonstrate functionality.
            Carlow = 'Carlow'
            Cork = 'Cork'
            Dublin = 'Dublin'
            Kildare = 'Kildare'
            Laois = 'Laois'
            Limerick = 'Limerick'
            Louth = 'Louth'
            Meath = 'Meath'
            Offaly = 'Offaly'
            Wicklow = 'Wicklow'
    	
	county = models.CharField(max_length=15, choices=Counties.choices(), default='None')
	contact_number = models.CharField(max_length=12, blank=False, null=False)
	personal_email = models.EmailField(blank=True, null=True) #Check exact syntax
	emergency_contact = models.CharField(max_length=50, blank=False, null=False)
	relationship_to_emergency_contact = models.CharField(max_length=30, blank=False, null=False)
	emergency_contact_number = models.CharField(max_length=12, blank=False, null=False)
	
	officer_pd = models.ForeignKey(Account, related_name='officer_pd', on_delete=models.CASCADE)
	last_updated = models.DateTimeField(auto_now=True)
	
	def __unicode__(self):
	    return self.county
	
	def __str__(self):
	    return "Personal Details for " + self.officer_pd