from django.db import models

designation_type = (
    ("MA'S", "MA'S"),
    ("CTS", "CTS")
)


class Doctor(models.Model):
    doctorId = models.AutoField(primary_key=True)
    phoneNumber = models.CharField(max_length=15, blank=False, null=False)
    name = models.CharField(max_length=50, blank=False, null=False)
    designation = models.CharField(max_length=15, choices=designation_type, blank=False, null=False)
    type = models.CharField(max_length=50, blank=False, null=False)
    password = models.CharField(max_length=15, blank=False, null=False)

    def __str__(self):
        return self.name
