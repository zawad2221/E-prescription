from django.urls import path
from .views import getMakePrescriptionPage,getMedicineOnId,getPatientsPhoneNumber,getPrescriptionMedicineOnId,getPatientNameOnId,getDoctorNameOnId,getPatientsNameOnPhoneNumber,getPatientOnNameAndPhoneNumber,getMedicine,getMedicineOnType,getMedicineOnCompany,getMedicineOnCompanyAndType,makePrescription,addMedicineOnPrescription,getSearchPrescriptionPage,getPrescriptionsOnPhoneNumber


urlpatterns = [
    path('getSearchPrescriptionPage/', getSearchPrescriptionPage, name="getSearchPrescriptionPage"),
    path('getSearchPrescriptionPage/getMedicineOnId', getMedicineOnId, name="getMedicineOnId"),
    path('getSearchPrescriptionPage/getPrescriptionMedicineOnId', getPrescriptionMedicineOnId, name="getPrescriptionMedicineOnId"),
    path('getSearchPrescriptionPage/getPatientNameOnId', getPatientNameOnId, name="getPatientNameOnId"),
    path('getSearchPrescriptionPage/getDoctorNameOnId', getDoctorNameOnId, name="getDoctorNameOnId"),
    path('getSearchPrescriptionPage/getPrescriptionsOnPhoneNumber', getPrescriptionsOnPhoneNumber, name="getPrescriptionsOnPhoneNumber"),
    path('getMakePrescriptionPage/', getMakePrescriptionPage, name="getMakePrescriptionPage"),
    path('getMakePrescriptionPage/getPatientPhoneNumber/', getPatientsPhoneNumber, name="getPatientPhoneNumber"),
    path('getMakePrescriptionPage/getPatientsNameOnPhoneNumber/', getPatientsNameOnPhoneNumber, name="getPatientsNameOnPhoneNumber"),
    path('getMakePrescriptionPage/getPatientOnNameAndPhoneNumber/', getPatientOnNameAndPhoneNumber, name="getPatientOnNameAndPhoneNumber"),
    path('getMakePrescriptionPage/getMedicine/', getMedicine, name="getMedicine"),
    path('getMakePrescriptionPage/getMedicineOnType/', getMedicineOnType, name="getMedicineOnType"),
    path('getMakePrescriptionPage/getMedicineOnCompany/', getMedicineOnCompany, name="getMedicineOnCompany"),
    path('getMakePrescriptionPage/getMedicineOnCompanyAndType/', getMedicineOnCompanyAndType, name="getMedicineOnCompanyAndType"),
    #post method don't accept / in end of the url
    path('getMakePrescriptionPage/makePrescription', makePrescription, name="makePrescription"),
    path('getMakePrescriptionPage/addMedicineOnPrescription', addMedicineOnPrescription, name="addMedicineOnPrescription"),
    

]