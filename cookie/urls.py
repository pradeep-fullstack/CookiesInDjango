from django.urls import path
from.import views

urlpatterns = [
     path('',views.index,name="index"),
     path('setcookie',views.setcookie,name="setcookie"),
     path('getcookie',views.getcookie,name="getcookie"),
  ]