from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='phonelist-home'),
    path('waiting/', views.waiting, name='phonelist-waiting'),
    path('riding/', views.riding, name='phonelist-riding'),
    path('done/', views.done, name='phonelist-done'),
    path('cancelled/', views.cancelled, name='phonelist-cancelled'),
    path('deleted/', views.deleted, name='phonelist-deleted'),
    path('add_ride/', views.add_ride, name='phonelist-addride'),
]
