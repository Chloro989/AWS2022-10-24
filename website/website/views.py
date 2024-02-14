from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse


class TopView(TemplateView):
    template_name = "index.html"


class ApexDataView(TemplateView):
    template_name = "apex_data.html"


class TimerView(TemplateView):
    template_name = "timer.html"

class StudyTopView(TemplateView):
    template_name = "study_top.html"

class JukenSugakuView(TemplateView):
    template_name = "juken_sugaku.html"

def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow: /admin/",  # クローラーがアクセスすべきでないパス
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")