from django.urls import path
from .views import login,logout


urlpatterns = [
    path('', login, name="login"),
    path('logout', logout, name="logout"),
]
