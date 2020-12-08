from django.shortcuts import render, redirect
from Company.models import Medicine
from Pharmacist.models import *
from django.utils import timezone
from Patient.models import Prescription, Patient, PrescribedMedicine
from django.contrib import messages

def orderMedicine(request):
    try:
      if request.method == "POST":

        if request.POST.get('quantity'):
            quantity=request.POST.get('quantity')
            print(quantity)
            mid = request.POST.get('mid')
            addOrder(request,mid,quantity,1)
            return redirect(myOrders)

        medicineCode = request.POST.get('medicineCode')
        medicines = addOrder(request,medicineCode,0)
        return render(request, "Pharmacist/pharmacist_order_medicine.html", {'medicines': medicines})

      else:
        return render(request, "Pharmacist/pharmacist_order_medicine.html")
    except:
        return render(request, "Pharmacist/pharmacist_order_medicine.html")


def addOrder(request,medicineCode,quantity,order=None):
    pid = request.session.get('id')
    pharmacist = Pharmacist.objects.get(pharmacistId=pid)
    mediciness = Medicine.objects.get(medicineId=medicineCode)
    comId=mediciness.company.companyId
    company=Company.objects.get(companyId=comId)
    medicines = Medicine.objects.all().filter(medicineId=medicineCode)

    if order:
        print ('Before order')
        orders = Order(medicine=mediciness, company=company, pharmacist=pharmacist, quantity=quantity, confirmationState='Pending')
        orders.save()
        print('After order')
        return order
    return medicines




def sellMedicine(request):
    try:
     if request.POST.get('search'):
        number = request.POST.get('number')
        request.session['number'] = number
        patient = Patient.objects.get(patientPhoneNumber=number)
        prescriptions = Prescription.objects.all().filter(prescriptionPatient=patient)

        return render(request, "Pharmacist/pharmacist_sell_medicine.html", {'prescriptions': prescriptions})

     elif request.POST.get('view'):
        number = request.session.get('number')
        patient = Patient.objects.get(patientPhoneNumber=number)
        prescriptions = Prescription.objects.all().filter(prescriptionPatient=patient)
        presid = request.POST.get('presid')
        request.session['presid'] = presid
        prescription = Prescription.objects.get(prescriptionId=presid)
        prescribedMedicines = PrescribedMedicine.objects.all().filter(prescribedMedicinePrescriptioin=prescription)
        print (prescribedMedicines)

        return render(request, "Pharmacist/pharmacist_sell_medicine.html",{'prescriptions': prescriptions,'prescribedMedicines': prescribedMedicines})

     elif request.POST.get('details'):
        number = request.session.get('number')
        patient = Patient.objects.get(patientPhoneNumber=number)
        prescriptions = Prescription.objects.all().filter(prescriptionPatient=patient)
        presid = request.session.get('presid')
        prescription = Prescription.objects.get(prescriptionId=presid)
        prescribedMedicines = PrescribedMedicine.objects.all().filter(prescribedMedicinePrescriptioin=prescription)
        presMedid = request.POST.get('presMedid')
        request.session['presMedid'] = presMedid
        prescribedMedicine = PrescribedMedicine.objects.all().filter(prescribedMedicineId=presMedid)

        return render(request, "Pharmacist/pharmacist_sell_medicine.html",{'prescriptions': prescriptions,'prescribedMedicines': prescribedMedicines,'prescribedMedicine':prescribedMedicine})

     elif request.POST.get('sell'):
        number = request.session.get('number')
        patient = Patient.objects.get(patientPhoneNumber=number)
        prescriptions = Prescription.objects.all().filter(prescriptionPatient=patient)
        presid = request.session.get('presid')
        prescription = Prescription.objects.get(prescriptionId=presid)
        prescribedMedicines = PrescribedMedicine.objects.all().filter(prescribedMedicinePrescriptioin=prescription)
        presMedid = request.session.get('presMedid')
        print (presMedid)
        prescribedMedicine = PrescribedMedicine.objects.all().filter(prescribedMedicineId=presMedid)
        preMedObj=PrescribedMedicine.objects.get(prescribedMedicineId=presMedid)
        medQuantity=preMedObj.prescribedMedicineQuantity
        medTaken=preMedObj.prescribedMedicineTakenQuantity

        pid = request.session.get('id')
        pharmacistObj = Pharmacist.objects.get(pharmacistId=pid)
        stocks= MedicineStock.objects.all().filter(pharmacist=pharmacistObj)

        preMedId=preMedObj.prescribedMedicineMedicine.medicineId

        quantity = int(request.POST.get('quantity'))
        medTaken=medTaken+quantity
        if medTaken<=medQuantity:
             for stock in stocks:
                 if stock.medicine.medicineId==preMedId:
                     if stock.quantity>=quantity:
                         preMedObj.prescribedMedicineTakenQuantity = medTaken
                         preMedObj.save()
                         stock.quantity=stock.quantity-quantity
                         stock.save()
                         soldMedicine = SoldMedicine(pharmacist=pharmacistObj, prescribedMedicine=preMedObj, medicineQuantity=quantity)
                         soldMedicine.save()
                     else:
                         messages.info(request, 'Sell Error! Medicine stock not enough!')
                 else:
                     messages.info(request, 'Sell Error! Medicine not available!')

        else:
            messages.info(request, 'Sell Error! Taken level crossed quantity limit!')

        return render(request, "Pharmacist/pharmacist_sell_medicine.html",{'prescriptions': prescriptions,'prescribedMedicines': prescribedMedicines,'prescribedMedicine':prescribedMedicine})

     return render(request, "Pharmacist/pharmacist_sell_medicine.html")

    except:
     return render(request, "Pharmacist/pharmacist_sell_medicine.html")




def medicineStock(request):
    pid = request.session.get('id')
    pharmacistObj = Pharmacist.objects.get(pharmacistId=pid)
    medicineStocks = MedicineStock.objects.all().filter(pharmacist=pharmacistObj)
    return render(request, "Pharmacist/pharmacist_medicine_stock.html", {'medicineStocks': medicineStocks})

def dashboard(request):
    return render(request, "Pharmacist/pharmacist_dashboard.html")

def myOrders(request):
    pid = request.session.get('id')
    pharmacists = Pharmacist.objects.get(pharmacistId=pid)
    orders = Order.objects.all().filter(pharmacist=pharmacists)
    return render(request, "Pharmacist/pharmacist_my_order_list.html", {'orders': orders})

def sellMedicineWithoutPrescription(request):
    try:
        if request.POST.get('search'):
            medCode = request.POST.get('medCode')
            request.session['medCode'] = medCode
            medicines = Medicine.objects.all().filter(medicineId=medCode)
            return render(request, "Pharmacist/pharmacist_sell_medicine_without_prescription.html",{'medicines': medicines})
        elif request.POST.get('sell'):
            quantity = int(request.POST.get('quantity'))
            medCode= int(request.session.get('medCode'))
            medicine = Medicine.objects.get(medicineId=medCode)
            pid = request.session.get('id')
            pharmacistObj = Pharmacist.objects.get(pharmacistId=pid)
            stocks= MedicineStock.objects.all().filter(pharmacist=pharmacistObj)
            print (stocks)
            for stock in stocks:
                if stock.medicine.medicineId == medCode:
                  print (221)
                  if stock.quantity >= quantity:
                    print (222)
                    soldMedicineWithoutPrescription=SoldMedicineWithoutPrescription(medicine=medicine,pharmacist=pharmacistObj,quantity=quantity)
                    soldMedicineWithoutPrescription.save()
                    stock.quantity = stock.quantity - quantity
                    stock.save()
                    return render(request, "Pharmacist/pharmacist_sell_medicine_without_prescription.html")
                  else:
                   messages.info(request, 'Sell Error! Medicine stock not enough!')
                else:
                  messages.info(request, 'Sell Error! Medicine not available!')
        return render(request, "Pharmacist/pharmacist_sell_medicine_without_prescription.html")
    except:
        return render(request, "Pharmacist/pharmacist_sell_medicine_without_prescription.html")

