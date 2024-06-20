
from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',admin_login, name='admin_login'),
    path('admindashboard/',admin_dashboard, name='admin_dashboard'),
    path('emacountssector/', ema_counts_sectors, name='ema_counts_sectors'),
    path('emacountsstocks/', ema_counts_stocks, name='ema_counts_stocks'),
    path('financialdata/',financial_data, name='financial_data'),
    path('sectordata/',sector_data, name='sector_data'),

]
