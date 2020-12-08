from django.db import models
from Doctor.models import Doctor
from Company.models import Medicine


# Create your models here.


class PatientSex(models.Model):
    patientSexId = models.AutoField(primary_key=True)
    patientSexName = models.CharField(max_length=8,blank=False,null=False)

    def __int__(self):
        return self.patientSexId


class PatientBloodGroup(models.Model):
    patientBloodGroupId = models.AutoField(primary_key=True)
    patientBloodGroupName = models.CharField(max_length=8, blank=False, null=False)

    def __str__(self):
        return self.patientBloodGroupName


class Patient(models.Model):
    patientId = models.AutoField(primary_key=True)
    patientName = models.CharField(max_length=44, blank=False, null=False)
    patientDateOfBirth = models.DateField(null=False,blank=False)
    patientSex = models.ForeignKey(PatientSex, on_delete=models.CASCADE, default=1, blank=False,null=False)
    patientPhoneNumber = models.CharField(max_length=16, blank=False, null=False)
    patientBloodGroup = models.ForeignKey(PatientBloodGroup, on_delete=models.CASCADE, default=1, blank=False, null=False)
    patientPassword = models.CharField(max_length=33, null=False, blank=False)

    def __int__(self):
        return self.patientId

class Prescription(models.Model):
    prescriptionId = models.AutoField(primary_key=True)
    prescriptionIssueDate = models.CharField(max_length=33,null=False,blank=False)
    prescriptionPatient = models.ForeignKey(Patient,on_delete=models.CASCADE,null=False,blank=False)
    prescriptionDoctor = models.ForeignKey(Doctor,on_delete=models.CASCADE,null=False,blank=False)

    def __int__(self):
        return self.prescriptionId

class PrescribedMedicine(models.Model):
    prescribedMedicineId = models.AutoField(primary_key=True)
    prescribedMedicineFrequancy = models.CharField(max_length=11,null=False,blank=False)
    prescribedMedicineFrequancyQuantity = models.CharField(max_length=11)
    prescribedMedicineDuration = models.CharField(max_length=11,null=False,blank=False)
    prescribedMedicineMedicine = models.ForeignKey(Medicine,on_delete=models.CASCADE,null=False,blank=False)
    prescribedMedicineQuantity = models.CharField(max_length=11)
    prescribedMedicineTakenQuantity = models.CharField(max_length=11)
    prescribedMedicinePrescription = models.ForeignKey(Prescription,on_delete=models.CASCADE,null=False,blank=False)
    
    def __int__(self):
        return self.prescribedMedicineId



