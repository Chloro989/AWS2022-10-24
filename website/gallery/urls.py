from django.urls import path
from . import views

urlpatterns = [
    path("gallery", views.gallery, name="gallery"),
    path("hallery/photo/<str:pk>/", views.viewPhoto, name="photo"),
    path("gallery/add/", views.addPhoto, name="add"),
]
