from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('kariyer',views.kariyer,name="kariyer"),
    path('egitim',views.egitim,name="egitim"),
    path('hakkimizda',views.hakkimizda,name="hakkimizda")
]