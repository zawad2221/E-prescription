from django.urls import path
from Patient.views import reportSuspiciousSoldMedicine,getPrescribedMedicineMedicineOnId,getPharmacistOnId,getSoldMedicineOnPatietnId,getPrescriptionReportPage,getMedicineOnId,getPrescriptionMedicineOnId,seePrescription,getPrescriptionsOnId,getDoctorNameOnId,getPatientNameOnId

urlpatterns = [

    path('seePrescription/', seePrescription, name="seePrescription"),
    path('seePrescription/getPrescriptionsOnId', getPrescriptionsOnId, name="getPrescriptionsOnId"),
    path('seePrescription/getDoctorNameOnId', getDoctorNameOnId, name="getDoctorNameOnId"),
    path('seePrescription/getPatientNameOnId', getPatientNameOnId, name="getPatientNameOnId"),
    path('seePrescription/getPrescriptionMedicineOnId', getPrescriptionMedicineOnId, name="getPrescriptionMedicineOnId"),
    path('seePrescription/getMedicineOnId', getMedicineOnId, name="getMedicineOnId"),
    path('getPrescriptionReportPage/',getPrescriptionReportPage,name="getPrescriptionReportPage"),
    path('getPrescriptionReportPage/getSoldMedicineOnPatietnId',getSoldMedicineOnPatietnId,name="getSoldMedicineOnPatietnId"),
    path('getPrescriptionReportPage/getPharmacistOnId',getPharmacistOnId,name="getPharmacistOnId"),
    path('getPrescriptionReportPage/getPrescribedMedicineMedicineOnId',getPrescribedMedicineMedicineOnId,name="getPrescribedMedicineMedicineOnId"),
    path('getPrescriptionReportPage/reportSuspiciousSoldMedicine',reportSuspiciousSoldMedicine,name="reportSuspiciousSoldMedicine")
    

]