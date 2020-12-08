from django.shortcuts import redirect, render
from Patient.models import Patient,PatientBloodGroup, PatientSex,Prescription,PrescribedMedicine
from Company.models import Company, Medicine, MedicineType
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from Account import views
from Patient.models import Patient
from .models import Doctor
from django.db import connection

# Create your views here.

def getSearchPrescriptionPage(request):
    if request.method=="GET":
        doctorId = request.session.get('id')
        userType = request.session.get('userType')
        print("type")
        print(userType)
        if 'userType' not in request.session:
            return redirect(views.login)
        if 'id' not in request.session:
            return redirect(views.login)
        if userType!="doctor":
            return redirect(views.login)
        return render(request,"Doctor/doctor_search_prescription.html")

def getMakePrescriptionPage(request):
    doctorId = request.session.get('id')
    userType = request.session.get('userType')
    print("type")
    print(userType)
    if 'userType' not in request.session:
        return redirect(views.login)
    if 'id' not in request.session:
        return redirect(views.login)
    if userType!="doctor":
        return redirect(views.login)

    patientBloodGroup = PatientBloodGroup.objects.all()
    companys = Company.objects.values('companyId','name').order_by('name')
    medicineTypes = MedicineType.objects.values('medicineTypeId','medicineTypeName').order_by('medicineTypeName')
    patientSexes = PatientSex.objects.all()
    medicines = Medicine.objects.all()
    for pa in medicineTypes:
            print(pa)
    return render(request, "Doctor/doctor_make_prescription.html", {'patientBloodGroup': patientBloodGroup,'companys': companys, 'medicineTypes': medicineTypes, 'patientSexes': patientSexes,'medicines':medicines})

def getPatientsPhoneNumber(request):
    if request.method=="GET":
        
        patientPhoneNumber = Patient.objects.all()
        for pa in patientPhoneNumber:
            print(pa)
        SomeModel_json = serializers.serialize("json", patientPhoneNumber,fields=('patientPhoneNumber'))
        
    return JsonResponse({'patientPhoneNumber' : SomeModel_json})

def getPatientsNameOnPhoneNumber(request):
    if request.method=="GET":
        patientPhoneNumber = request.GET['patientPhoneNumber']
        patientName = Patient.objects.filter(patientPhoneNumber=patientPhoneNumber)
        for pa in patientName:
            print(pa.patientName)
        SomeModel_json = serializers.serialize("json", patientName,fields=('patientName'))
    return JsonResponse({'patientName': SomeModel_json})

def getPatientOnNameAndPhoneNumber(request):
    if request.method=="GET":
        patientName = request.GET['patientName']
        patientPhoneNumber = request.GET['patientPhoneNumber']
        patient = Patient.objects.filter(patientName=patientName,patientPhoneNumber=patientPhoneNumber)
        for pa in patient:
            print("sex")
            print(pa.patientDateOfBirth)
        
        SomeModel_json = serializers.serialize("json", patient,fields=('patientId', 'patientName','patientDateOfBirth','patientSex','patientBloodGroup','patientPhoneNumber'))
        return JsonResponse({'patient': SomeModel_json})

def getMedicine(request):
    if request.method=="GET":
        
        medicines = Medicine.objects.all().order_by('medicineName')
        for pa in medicines:
           print(pa.medicineName)
        medicineInJson = serializers.serialize("json",medicines,fields=('medicineId','medicineName'))
        return JsonResponse({"medicines": medicineInJson})


def getMedicineOnType(request):
    if request.method=="GET":
        medicineTypeId = request.GET['medicineTypeId']
        medicine = Medicine.objects.filter(type=medicineTypeId)
        medicineInJson = serializers.serialize("json",medicine,fields=('medicineId','medicineName'))
        return JsonResponse({"medicine": medicineInJson})

def getMedicineOnCompany(request):
    if request.method=="GET":
        medicineCompanyId = request.GET['medicineCompanyId']
        medicine = Medicine.objects.filter(company=medicineCompanyId)
        for pa in medicine:
            print(pa.medicineId)
        medicineInJson = serializers.serialize("json",medicine,fields=('medicineId','medicineName'))
        return JsonResponse({"medicine": medicineInJson})

def getMedicineOnCompanyAndType(request):
    if request.method=="GET":
        medicineCompanyId = request.GET['medicineCompanyId']
        medicineTypeId = request.GET['medicineTypeId']
        print(medicineCompanyId)
        print(medicineTypeId)
        medicines = Medicine.objects.filter(type=medicineTypeId,company=medicineCompanyId)
        medicineInJson = serializers.serialize("json",medicines,fields=('medicineId','medicineName'))
        return JsonResponse({"medicines": medicineInJson})

def regPatient(patientPhoneNumber,patientName,patientBloodGroupId,patientDateOfBirth,patientSexId):
    patientSex= PatientSex.objects.get(patientSexId=patientSexId)
    patientBloodGroup=PatientBloodGroup.objects.get(patientBloodGroupId=patientBloodGroupId)
    patient= Patient(patientName=patientName,patientDateOfBirth=patientDateOfBirth,patientSex=patientSex,patientPhoneNumber=patientPhoneNumber,patientBloodGroup=patientBloodGroup,patientPassword=patientPhoneNumber)
    patient.save()
    return patient

def getPatient(patientPhoneNumber,patientName,patientBloodGroupId,patientDateOfBirth,patientSexId):
    patient = Patient.objects.filter(patientPhoneNumber=patientPhoneNumber,patientName=patientName)
    if patient.exists():
            for pa in patient:
              patientId=pa.patientId  
    else:
        patient=regPatient(patientPhoneNumber,patientName,patientBloodGroupId,patientDateOfBirth,patientSexId)
        patient = Patient.objects.filter(patientId=patient.patientId)
    return patient


def makePrescription(request):
    if request.method=="POST":
        doctorId = request.session.get('id')
        patientPhoneNumber=request.POST['patientPhoneNumber']
        patientName=request.POST['patientName']
        patientSexId=request.POST['patientSexId']
        patientBloodGroupId=request.POST['patientBloodGroupId']
        patientDateOfBirth=request.POST['patientDateOfBirth']
        #medicine= request.POST['medicines']
        #print(medicine)
        print(patientPhoneNumber)
        print(patientName)
        patient = getPatient(patientPhoneNumber,patientName,patientBloodGroupId,patientDateOfBirth,patientSexId)

        for pa in patient:
              patient=pa.patientId
        patient = Patient.objects.get(patientId=patient)
        doctor = Doctor.objects.get(doctorId=doctorId)
        priscription = Prescription(prescriptionIssueDate="11/30/2019",prescriptionPatient=patient,prescriptionDoctor=doctor)
        priscription.save()

        prescriptionId=priscription.prescriptionId
        priscription = Prescription.objects.filter(prescriptionId=prescriptionId)

        #print(patientId)
        priscriptionJson = serializers.serialize("json",priscription)
        return JsonResponse({"priscriptions": priscriptionJson})

def addMedicineOnPrescription(request):
    if request.method=="POST":
        prescribedMedicineFrequancy=request.POST['prescribedMedicineFrequancy']
        prescribedMedicineFrequancyQuantity=request.POST['prescribedMedicineFrequancyQuantity']
        prescribedMedicineDuration=request.POST['prescribedMedicineDuration']
        prescribedMedicineMedicine=request.POST['medicineId']
        prescribedMedicineQuantity=request.POST['prescribedMedicineQuantity']
        prescribedMedicineTakenQuantity=request.POST['prescribedMedicineTakenQuantity']
        prescribedMedicinePrescription=request.POST['prescriptionId']
        print(prescribedMedicineFrequancy)

        medicine = Medicine.objects.get(medicineId=prescribedMedicineMedicine)
        prescription = Prescription.objects.get(prescriptionId=prescribedMedicinePrescription)

        prescribedMedicine = PrescribedMedicine(prescribedMedicineFrequancy=prescribedMedicineFrequancy,prescribedMedicineFrequancyQuantity=prescribedMedicineFrequancyQuantity,prescribedMedicineDuration=prescribedMedicineDuration,prescribedMedicineMedicine=medicine,prescribedMedicineQuantity=prescribedMedicineQuantity,prescribedMedicineTakenQuantity=prescribedMedicineTakenQuantity,prescribedMedicinePrescription=prescription)
        prescribedMedicine.save()
        return HttpResponse("added")

def getPrescriptionsOnPhoneNumber(request):
    if request.method=="GET":
        phoneNumber = request.GET['phoneNumber']
        #patients = Patient.objects.get(patientPhoneNumber=phoneNumber)

        prescriptions = Prescription.objects.raw("select prescriptionId from patient_prescription inner join patient_patient on patient_patient.patientId=patient_prescription.prescriptionPatient_Id where patientPhoneNumber='"+phoneNumber+"'")
        
        for pre in prescriptions:
            print(pre.prescriptionId)

        # cursor = connection.cursor()
        # cursor.execute("select * from patient_prescription inner join patient_patient on patient_patient.patientId=patient_prescription.prescriptionPatient_Id where patientPhoneNumber='22222222222'")
        # for row in cursor:
        #     print(row[0])
        priscriptionJson = serializers.serialize("json",prescriptions)
        return JsonResponse({"priscriptions": priscriptionJson})
        # return HttpResponse(prescriptions)

def getPatientNameOnId(request):
    if request.method=="GET":
        patientId=request.GET['patientId']
        patient = Patient.objects.filter(patientId=patientId)
        patientJson = serializers.serialize("json",patient,fields=('patientName'))
        return JsonResponse({"patientName":patientJson})
        
def getDoctorNameOnId(request):
    if request.method=="GET":
        doctorId=request.GET['doctorId']
        doctor = Doctor.objects.filter(doctorId=doctorId)
        doctorJson = serializers.serialize("json",doctor,fields=('name'))
        return JsonResponse({"doctorName":doctorJson})

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