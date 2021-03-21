from django.db import models
from account.models import Account
from account.utils import ChoiceEnum
from datetime import datetime
from django.contrib import messages
from .utils import checkForLateClocking

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
    number_of_clockings = models.IntegerField(default=0)
    clocking_in_time = models.TimeField(blank=True, null=True)
    clocking_out_time = models.TimeField(blank=True, null=True)
    lunch_out_time = models.TimeField(blank=True, null=True)
    lunch_in_time = models.TimeField(blank=True, null=True)
    #clocking_date = models.DateField(blank=True, null=True)
    
    def __unicode__(self):
        return self.roster_shift_label
        
    def __str__(self):
        if self.roster_due_on == False:
            return str(self.roster_officer_id.username) + " : " + str(self.roster_shift_date) + " : " + str(self.roster_shift_label)
        else:
            return str(self.roster_officer_id.username) + " : " + str(self.roster_shift_date) + " : " + str(self.roster_shift)
            
    def updateCorrectClocking(self, request):
        if self.number_of_clockings == 0:
            t = datetime.now().time()
            self.clocking_in_time = t.replace(microsecond=0)
            #print("Clock In: " + str(self.clocking_in_time))
            officer = self.roster_officer_id
            checkForLateClocking(t, officer)
            messages.success(request, "Clock In completed.")
        elif self.number_of_clockings == 1:
            t = datetime.now().time()
            self.lunch_out_time = t.replace(microsecond=0)
            #print("Lunch Out: " + str(self.lunch_out_time))
            messages.success(request, "Lunch Out clock completed.")
        elif self.number_of_clockings == 2:
            t = datetime.now().time()
            self.lunch_in_time = t.replace(microsecond=0)
            #print("Lunch In: " + str(self.lunch_in_time))
            messages.success(request, "Lunch In clock completed.")
        else:
            t = datetime.now().time()
            self.clocking_out_time = t.replace(microsecond=0)
            #print("Clock Out: " + str(self.clocking_out_time))
            messages.success(request, "Clock Out completed.")
        self.number_of_clockings += 1
        return self.save()
            
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
	    return "Personal Details for " + str(self.officer_pd)
	    
class ManualClocking(models.Model):
	mc_officer_id = models.ForeignKey(Account,related_name='mc_officer_id', on_delete=models.CASCADE)
	clocking_date = models.DateField(blank=False, null=False)
	clocking_in_time = models.TimeField(blank=False, null=False)
	clocking_out_time = models.TimeField(blank=False, null=False)
	lunch_out_time = models.TimeField(blank=False, null=False)
	lunch_in_time = models.TimeField(blank=False, null=False)
	reason_for_missed_clocking = models.CharField(max_length=200, blank=False, null=False)
	checked_by_validator = models.BooleanField(default=False)
	validator_id = models.ForeignKey(Account, related_name='validator_id', on_delete=models.CASCADE, blank=True, null=True)
	accept_reject_clock = models.BooleanField(default=False)
	reason_manual_clock_rejected = models.TextField(max_length=400, blank=True, null=True)
	
	
	def __unicode__(self):
		return self.clocking_date
		
		
	def __str__(self):
		return str(self.mc_officer_id) + " manual clock for " + str(self.clocking_date)
		
class Lates(models.Model):
    lates_officer_id = models.ForeignKey(Account,related_name='lates_officer_id', on_delete=models.CASCADE)
    date_of_late = models.DateField(blank=False, null=False)
    late_clocking_time = models.TimeField(blank=False, null=False)
    duration_of_late = models.DurationField(blank=False, null=False)
    
    def __unicode__(self):
        return self.date_of_late
    
    def __str__(self):
	    return str(self.lates_officer_id) + " was late on " + str(self.date_of_late) + " by " + str(self.duration_of_late)
	    
class LatesPerYear(models.Model):
    yearly_lates_officer_id = models.ForeignKey(Account, related_name='yearly_lates_officer_id', on_delete=models.CASCADE)
    lates_year = models.IntegerField(blank=False, null=False)
    number_lates_for_year = models.IntegerField(blank=False, null=False)
    
    def __unicode__(self):
        return self.lates_year
        
    def __str__(self):
        return str(self.yearly_lates_officer_id) + " has had " + str(self.number_lates_for_year) + " lates in " + str(self.lates_year)
        
