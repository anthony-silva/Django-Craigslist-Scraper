from django.urls import path
from . import views

urlpatterns = [
    path('', views.CraigslistIndexView, name='home'),
    path('results/', views.CraigslistResultsView, name='search')
]
