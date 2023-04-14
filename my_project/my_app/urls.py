from django.urls import path
from . import views

urlpatterns = [
    path('persons/', views.get_all_persons, name='get_all_persons'),
    path("persons/create/", views.create_person, name="create_person"),
    
]
