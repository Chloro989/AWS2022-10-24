from django.contrib import admin
from django.urls import path
from .views import TopView, ApexDataView, TimerView
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TopView.as_view(), name="top"),
    path("apex_data/", ApexDataView.as_view(), name="apex_data"),
    path("", include("guessing_number.urls")),
    path("timer/", TimerView.as_view(), name="timer"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
