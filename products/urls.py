from django.urls import path
from . import views

urlpatterns = [path("", views.index,name="index"),
               path("aboutus/", views.aboutus,name="aboutus"),
               path("kitchen/", views.kitchen,name="kitchen"),
               path("engeneering/", views.engeneering,name="engeneering"),
               path("spa/", views.spa,name="spa"),
               path("contact/", views.contact,name="contact"),
               path("send_email/", views.send_email,name="send_email"),
               ]