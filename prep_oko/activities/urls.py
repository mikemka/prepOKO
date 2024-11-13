from django.urls import path
from . import views


app_name = 'activities'

urlpatterns = [
    path('', views.ActivitiesView.as_view(), name='main'),
    path('<int:form_id>/', views.ActivitiesView.as_view(), name='main_with_id'),
    path('<int:form_id>/new/', views.NewActivityView.as_view(), name='new'),
]
