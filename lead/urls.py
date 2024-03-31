from django.urls import path

from . import views

app_name = 'lead'

urlpatterns = [
    path('', views.leads_list, name='leads_list'),
    path('add-lead/', views.add_lead, name='add_lead')
]