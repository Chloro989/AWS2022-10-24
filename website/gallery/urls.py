from django.urls import path
from .views import LicenseView
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemap import CategorySitemap, PhotoSitemap

urlpatterns = [
    path("gallery", views.gallery, name="gallery"),
    path("gallery/photo/<str:pk>/", views.viewPhoto, name="photo"),
    path("gallery/add/", views.addPhoto, name="add"),
    path("gallery/license/", LicenseView.as_view(), name="license"),
    path("gallery/photo/<str:pk>/delete/", views.deletePhoto, name="delete_photo"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemap}, name='django.contrib.sitemaps.views.sitemap'),
]

sitemaps = {
    'categories': CategorySitemap,
    'photos': PhotoSitemap,
}