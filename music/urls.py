from django.contrib import admin
from django.urls import path
from .app.FuckYourMusic import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home),
    path('sw.js',
        views.ServiceWorkerView.as_view(),
        name=views.ServiceWorkerView.name,
    ),
]
