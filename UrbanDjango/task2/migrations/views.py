from django.shortcuts import render
from django.views.generic import TemplateView


def func_templates(request):
    return render(request, "second_task/class_template.html")


class ClassTemplates(TemplateView):
    template_name = "class_template.html"