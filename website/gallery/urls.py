from django.urls import path
from .views import LicenseView
from . import views

urlpatterns = [
    path("gallery", views.gallery, name="gallery"),
    path("gallery/photo/<str:pk>/", views.viewPhoto, name="photo"),
    path("gallery/add/", views.addPhoto, name="add"),
    path("gallery/license/", LicenseView.as_view(), name="license"),
    path("gallery/photo/<str:pk>/delete/", views.deletePhoto, name="delete_photo"),
]
