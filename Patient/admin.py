from django.contrib import admin

# Register your models here.
from Patient.models import Patient, PatientBloodGroup, PatientSex, Prescription, PrescribedMedicine

admin.site.register(Patient)
admin.site.register(PatientSex)
admin.site.register(PatientBloodGroup)
admin.site.register(Prescription)
admin.site.register(PrescribedMedicine)

