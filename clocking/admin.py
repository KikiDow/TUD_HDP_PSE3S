from django.contrib import admin
from .models import Quarter, Shift, RosterSideA, RosterSideB, Roster, PersonalDetails, ManualClocking

# Register your models here.
admin.site.register(Quarter)
admin.site.register(Shift)
admin.site.register(RosterSideA)
admin.site.register(RosterSideB)
admin.site.register(Roster)
admin.site.register(PersonalDetails)
admin.site.register(ManualClocking)