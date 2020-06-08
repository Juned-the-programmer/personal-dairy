from django.urls import path
from pages import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup/', views.signup , name='signup'),
    path('login/', views.login , name='login'),
    path('list/',views.list,name='list'),
    path('listdisplay/<pk>',views.listdisplay,name='listdisplay'),
    path('logout/',views.logout,name='logout')
]
