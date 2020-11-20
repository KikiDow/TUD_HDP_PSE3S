from django.contrib import admin
from .models import Overtime, OvertimePerQtr, AvailabilitySheet, ShortTermAvailabilty, NonScheduledOvertimeRequest, AllowancesRequest, ShortOvertime
# Register your models here.
admin.site.register(Overtime)
admin.site.register(OvertimePerQtr)
admin.site.register(AvailabilitySheet)
admin.site.register(ShortTermAvailabilty)
admin.site.register(NonScheduledOvertimeRequest)
admin.site.register(AllowancesRequest)
admin.site.register(ShortOvertime)
