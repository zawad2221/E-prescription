# Generated by Django 2.2.6 on 2019-12-06 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Doctor', '0001_initial'),
        ('Company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patientId', models.AutoField(primary_key=True, serialize=False)),
                ('patientName', models.CharField(max_length=44)),
                ('patientDateOfBirth', models.DateField()),
                ('patientPhoneNumber', models.CharField(max_length=16)),
                ('patientPassword', models.CharField(max_length=33)),
            ],
        ),
        migrations.CreateModel(
            name='PatientBloodGroup',
            fields=[
                ('patientBloodGroupId', models.AutoField(primary_key=True, serialize=False)),
                ('patientBloodGroupName', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='PatientSex',
            fields=[
                ('patientSexId', models.AutoField(primary_key=True, serialize=False)),
                ('patientSexName', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('prescriptionId', models.AutoField(primary_key=True, serialize=False)),
                ('prescriptionIssueDate', models.CharField(max_length=33)),
                ('prescriptionDoctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Doctor.Doctor')),
                ('prescriptionPatient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Patient.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='PrescribedMedicine',
            fields=[
                ('prescribedMedicineId', models.AutoField(primary_key=True, serialize=False)),
                ('prescribedMedicineFrequancy', models.CharField(max_length=11)),
                ('prescribedMedicineFrequancyQuantity', models.CharField(max_length=11)),
                ('prescribedMedicineDuration', models.CharField(max_length=11)),
                ('prescribedMedicineQuantity', models.CharField(max_length=11)),
                ('prescribedMedicineTakenQuantity', models.CharField(max_length=11)),
                ('prescribedMedicineMedicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company.Medicine')),
                ('prescribedMedicinePrescription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Patient.Prescription')),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='patientBloodGroup',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Patient.PatientBloodGroup'),
        ),
        migrations.AddField(
            model_name='patient',
            name='patientSex',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Patient.PatientSex'),
        ),
    ]
