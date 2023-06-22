from django.urls import path
from . import views
from .views import Homepage

urlpatterns=[
    path('',views.add_student,name='home!'),
    path('view/',Homepage.as_view(),name='success')
]