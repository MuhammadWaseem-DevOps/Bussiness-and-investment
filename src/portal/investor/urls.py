from django.urls import path, include

from . import views

app_name = 'investor'

urlpatterns = [
    path('dashboard/', views.InvestorDashboard.as_view(), name='dashboard')

]
