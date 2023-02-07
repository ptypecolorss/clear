from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


def home(request):
	return render(request, 'home.html')


class ServiceWorkerView(TemplateView):
    template_name = 'sw.js'
    content_type = 'application/javascript'
    name = 'sw.js'
