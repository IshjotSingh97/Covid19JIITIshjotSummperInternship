from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('urgent',views.urgent,name='urgent')
]