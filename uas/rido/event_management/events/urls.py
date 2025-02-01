

from django.urls import path
from . import views

urlpatterns = [
    path('acara/', views.daftar_acara, name='daftar_acara'),
    path('acara/<int:acara_id>/daftar/', views.daftar_peserta, name='daftar_peserta'),
]

