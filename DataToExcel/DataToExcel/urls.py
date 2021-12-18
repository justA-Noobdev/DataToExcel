from django.contrib import admin
from django.urls import path

from MyApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ExcelPageView.as_view(), name='home'), 
    path('export/excel', views.export_users_xls, name='export_excel'),
    path('export/excel-styling', views.export_styling_xls, name='export_styling_excel'),
    path('export/export-write-xls', views.export_write_xls, name='export_write_xls'),
]