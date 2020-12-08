from django.urls import path

from Pharmacist.views import orderMedicine, medicineStock, sellMedicine, dashboard, myOrders, sellMedicineWithoutPrescription

urlpatterns = [
    path('orderMedicine/', orderMedicine, name='orderMedicine'),
    path('sellMedicine/', sellMedicine, name='sellMedicine'),
    path('medicineStock/', medicineStock, name='medicineStock'),
    path('dashboard/', dashboard, name='dashboard'),
    path('myOrders/', myOrders, name='myOrders'),
    path('sellMedicineWithoutPrescription/', sellMedicineWithoutPrescription, name='sellMedicineWithoutPrescription'),
]