from django.urls import path
from .views import UserRegisterView,PatientListCreateView,HeartRateListCreateView,UserLoginView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),

    path('patient/', PatientListCreateView.as_view(), name='patient-list-create'),
    path('heartrate/', HeartRateListCreateView.as_view(), name='heart-rate-list-create'),


]