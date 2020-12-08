from django.shortcuts import render, redirect
from .models import Prescription,Patient
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from Doctor.models import Doctor
from Account import views

from Patient.models import Patient,PatientBloodGroup, PatientSex,Prescription,PrescribedMedicine
from Company.models import Company, Medicine, MedicineType
from Pharmacist.models import SoldMedicine,Pharmacist
from Report.models import SuspiciousSoldMedicineReport



# return patient prescription page
def seePrescription(request):
    doctorId = request.session.get('id')
    userType = request.session.get('userType')
    print("type")
    print(userType)
    if 'userType' not in request.session:
       return redirect(views.login)
    if 'id' not in request.session:
       return redirect(views.login)
    if userType!="patient":
        return redirect(views.login)
    return render(request, "Patient/patient_prescription.html")

def getPrescriptionReportPage(request):
    if request.method=="GET":
        return render(request,"Patient/patient_report.html")

def getPrescriptionsOnId(request):
    if request.method=="GET":
        patientId = request.session.get('id')
        prescriptions = Prescription.objects.raw("select prescriptionId from patient_prescription inner join patient_patient on patient_patient.patientId=patient_prescription.prescriptionPatient_Id where patientId='"+str(patientId)+"'")
        for pre in prescriptions:
            print(pre.prescriptionId)
        priscriptionJson = serializers.serialize("json",prescriptions)
        return JsonResponse({"priscriptions": priscriptionJson})

def getDoctorNameOnId(request):
    if request.method=="GET":
        doctorId=request.GET['doctorId']
        doctor = Doctor.objects.filter(doctorId=doctorId)
        doctorJson = serializers.serialize("json",doctor,fields=('name'))
        return JsonResponse({"doctorName":doctorJson})

def getPatientNameOnId(request):
    if request.method=="GET":
        patientId = request.session.get('id')
        patient = Patient.objects.filter(patientId=patientId)
        for pa in patient:
            print(pa.patientName)
        patientJson = serializers.serialize("json",patient,fields=('patientName'))
        return JsonResponse({"patientName":patientJson})

def getPrescriptionMedicineOnId(request):
    if request.method=="GET":
        prescriptionId = request.GET['prescriptionId']
        prescription = Prescription.objects.get(prescriptionId=prescriptionId)
        prescriptionMedicines = PrescribedMedicine.objects.filter(prescribedMedicinePrescription=prescription)
        prescriptionMedicineJson = serializers.serialize("json",prescriptionMedicines)
        return JsonResponse({"priscriptionMedicines": prescriptionMedicineJson})

def getMedicineOnId(request):
    if request.method=="GET":
        medicineId = request.GET['medicineId']
        medicine = Medicine.objects.filter(medicineId=medicineId)
        medicineJson = serializers.serialize("json",medicine)
        return JsonResponse({"medicine": medicineJson})

def getSoldMedicineOnPatietnId(request):
    if request.method=="GET":
        patientId = request.session.get('id')
        soldMedicine = SoldMedicine.objects.filter(prescribedMedicine__prescribedMedicinePrescription__prescriptionPatient__patientId=patientId)
        soldMedicineJson = serializers.serialize("json",soldMedicine)
        return JsonResponse({"soldMedicne":soldMedicineJson})

def getPharmacistOnId(request):
    if request.method=="GET":
        pharmacistId = request.GET['pharmacistId']
        pharmacist = Pharmacist.objects.filter(pharmacistId=pharmacistId)
        pharmacistJson = serializers.serialize("json",pharmacist)
        return JsonResponse({"pharmacist": pharmacistJson})

def getPrescribedMedicineMedicineOnId(request):
    if request.method=="GET":
        prescribedMedicineId=request.GET['prescribedMedicineId']
        #prescribedMedicine = PrescribedMedicine.objects.filter(prescribedMedicineId=prescribedMedicineId)
        prescribedMedicineMedicien = Medicine.objects.filter(prescribedmedicine__prescribedMedicineId=prescribedMedicineId)
        for p in prescribedMedicineMedicien:
            print(p.medicineName)
        prescribedMedicineMedicienJson = serializers.serialize("json",prescribedMedicineMedicien)
        return JsonResponse({"prescribedMedicineMedicine": prescribedMedicineMedicienJson})

def reportSuspiciousSoldMedicine(request):
    if request.method=="GET":
        patientId = request.session.get('id')
        soldMedicineId = request.GET['soldMedicineId']
        reportComent = request.GET['reportComent']
        pharmacistId = request.GET['pharmacistId']
        soldMedicine = SoldMedicine.objects.get(soldMedicineId=soldMedicineId)
        pharmacist = Pharmacist.objects.get(pharmacistId=pharmacistId)
        patient = Patient.objects.get(patientId=patientId)

        suspiciousSoldMedicineReport = SuspiciousSoldMedicineReport.objects.filter(soldMedicine=soldMedicine)
        if suspiciousSoldMedicineReport.exists():
            for pa in suspiciousSoldMedicineReport:
              suspiciousSoldMedicineReportId=pa.suspiciousSoldMedicineReportId 
        else:
            suspiciousSoldMedicineReport = SuspiciousSoldMedicineReport(soldMedicine=soldMedicine,reportComent=reportComent,pharmacist=pharmacist,patient=patient)
            suspiciousSoldMedicineReport.save()
            return HttpResponse("added")