from django.urls import path
from . import views

urlpatterns = [
    path('/', views.home, name="home"),
    path('/teammembers',views.teammembers,name="teammembers"),
    path('/bc-clients',views.bc_clients,name="bc_clients"),
    path('/capita-clients',views.capita_clients,name="capita_clients"),

    
]
