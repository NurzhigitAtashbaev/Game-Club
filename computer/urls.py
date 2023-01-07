from django import urls
from django.urls import path

# from .models import
from .views import general_computers, manage_computer, vip_computer

urlpatterns = [
    # path('', computer_details, name='computer'),
    path('general/', general_computers, name='general'),
    path('<int:pk>/', manage_computer, name='computer_detail'),
    path('vip/', vip_computer, name='vip')

]
