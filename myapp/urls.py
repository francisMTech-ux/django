
from django.urls import path
from myapp import views

urlpatterns=[

    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('blog/',views.blog,name='blog'),
    path('services/',views.services,name='services'),
    path('ourwork/',views.ourwork,name='our work'),
]