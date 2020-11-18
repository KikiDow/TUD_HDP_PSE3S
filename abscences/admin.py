from django.contrib import admin
from .models import CertifiedSickLeave, UnCertifiedSickLeave, ForceMajeure, CertifiedSickPerYear, UnCertifiedSickPerYear, ForceMajeurePerYear

# Register your models here.
admin.site.register(CertifiedSickLeave)
admin.site.register(UnCertifiedSickLeave)
admin.site.register(ForceMajeure)
admin.site.register(CertifiedSickPerYear)
admin.site.register(UnCertifiedSickPerYear)
admin.site.register(ForceMajeurePerYear)
