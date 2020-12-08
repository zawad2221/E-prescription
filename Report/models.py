from django.db import models

from Pharmacist.models import Pharmacist, SoldMedicine
from Patient.models import Patient
# Create your models here.

class SuspiciousSoldMedicineReport(models.Model):
    suspiciousSoldMedicineReportId = models.AutoField(primary_key=True)
    soldMedicine = models.ForeignKey(SoldMedicine,on_delete=models.CASCADE)
    reportComent = models.TextField(null=False,blank=False,max_length=100)
    pharmacist = models.ForeignKey(Pharmacist,on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)

    def __int__(self):
        return self.suspiciousSoldMedicineReportId