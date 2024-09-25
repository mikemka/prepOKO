from django.urls import path
from . import views


app_name = 'activities'

urlpatterns = [
    path('', views.ActivitiesView.as_view(), name='main'),
]