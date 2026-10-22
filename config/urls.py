from django.contrib import admin
from django.urls import path
from portal import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.inicio, name="inicio"),
    path("conteudo/<slug:slug>/", views.exibir_conteudo, name="conteudo"),
]
