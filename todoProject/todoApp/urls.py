from django.urls import path
from . import views

urlpatterns = [
    path('addTask/', views.addTask, name='addTask'),
    path('markAsDone/<int:id>', views.markAsDone, name='markAsDone'),
    path('setAsIncomplete/<int:id>', views.setAsIncomplete, name='setAsIncomplete')
]