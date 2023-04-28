from django.urls import path
from . import views

urlpatterns = [path("", views.index,name="index"),
               path("aboutus/", views.aboutus,name="aboutus"),
               path("kitchen/", views.kitchen,name="kitchen"),
               ]