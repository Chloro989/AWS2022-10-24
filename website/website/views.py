from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.shortcuts import render


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