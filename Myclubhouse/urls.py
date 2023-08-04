from django.urls import path
from Myclubhouse import controller
urlpatterns = [
    path('home/', controller.homepage,name="home"),
    path('about/', controller.about,name="ab"),
    path('contact/', controller.contact,name="con"),
    path('services/', controller.services,name="ser")
]