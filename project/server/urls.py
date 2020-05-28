from django.urls import path
from . import views

urlpatterns = [
    path('api/salary/', views.GetSalaryAPIView.as_view(), name='get_salary')
]