from django.contrib import admin
from django.urls import path
from .views import TopView,ApexDataView
from django.conf.urls import include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', TopView.as_view(), name='top'),
    path('apex_data/', ApexDataView.as_view(), name='apex_data'),
    path('', include('guessing_number.urls')),
]
