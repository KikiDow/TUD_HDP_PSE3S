from django.contrib import admin
from .models import AnnualLeaveRequest, AnnualLeaveCarriedOver, ShortTermAnnualLeaveRequest, AnnualLeave
# Register your models here.
admin.site.register(AnnualLeaveRequest)
admin.site.register(AnnualLeaveCarriedOver)
admin.site.register(ShortTermAnnualLeaveRequest)
admin.site.register(AnnualLeave)
