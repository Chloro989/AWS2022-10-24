from django.contrib import admin
from django.urls import path
from .views import TopView, ApexDataView, TimerView, StudyTopView,JukenSugakuView
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TopView.as_view(), name="top"),
    path("apex_data/", ApexDataView.as_view(), name="apex_data"),
    path("studies/", StudyTopView.as_view(), name="study_top"),
    path("studies/jkmath", JukenSugakuView.as_view(), name="jkmath"),
    path("", include("guessing_number.urls")),
    path("timer/", TimerView.as_view(), name="timer"),
    path("", include("gallery.urls")),
    path("accounts/", include("allauth.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
