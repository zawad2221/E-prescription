from django.db import models

medicine_type = (
    ("MA'S", "MA'S"),
    ("CTS", "CTS")
)


class Company(models.Model):
    companyId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25, blank=False, null=False)
    licence = models.CharField(max_length=50, blank=False, null=False)
    phoneNumber = models.CharField(max_length=15, blank=False, null=False)
    email = models.CharField(max_length=50, blank=False, null=False)
    address = models.CharField(max_length=50, blank=False, null=False)
    password = models.CharField(max_length=15, blank=False, null=False)

    def __str__(self):
        return self.name

class AntibioticType(models.Model):
    antibioticTypeId = models.AutoField(primary_key=True)
    antibioticTypeName = models.CharField(max_length=33)

    def __str__(self):
        return self.antibioticTypeName

class MedicineType(models.Model):
    medicineTypeId = models.AutoField(primary_key=True)
    medicineTypeName = models.CharField(max_length=33, blank=False, null=False)
    antibioticType = models.ForeignKey(AntibioticType,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.medicineTypeName


class MedicineForm(models.Model):
    medicineFormId = models.AutoField(primary_key=True)
    medicineFormName = models.CharField(max_length=33, blank=False, null=False)

    def __int__(self):
        return self.medicineFormId

# class Medicine(models.Model):
#     #company = models.ForeignKey(Company, on_delete=models.CASCADE)
#     companyNumber = models.CharField(max_length=11, blank=False, null=False)
#     medicineName = models.CharField(max_length=25, blank=False, null=False)
#     singleUnitQuantity = models.CharField(max_length=50, blank=False, null=False)
#     formName = models.CharField(max_length=15,choices=medicine_type, blank=False, null=False)
#     type = models.CharField(max_length=15, choices=medicine_type, blank=False, null=False)
#
#     def __str__(self):
#         return "{0},{1}".format(self.companyNumber,self.medicineName)





class Medicine(models.Model):
    medicineId = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    medicineName = models.CharField(max_length=25, blank=False, null=False)
    singleUnitQuantity = models.CharField(max_length=50, blank=False, null=False)
    form = models.ForeignKey(MedicineForm, on_delete=models.CASCADE)
    type = models.ForeignKey(MedicineType, on_delete=models.CASCADE)

    def __str__(self):
        return self.medicineName



