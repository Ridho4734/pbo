from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Acara, Peserta

def daftar_acara(request):
    acara = Acara.objects.all()
    return render(request, 'events/daftar_acara.html', {'acara': acara})

def daftar_peserta(request, acara_id):
    acara = get_object_or_404(Acara, id=acara_id)
    if request.method == 'POST':
        if acara.peserta_terdaftar < acara.kapasitas:
            nama = request.POST['nama']
            email = request.POST['email']
            Peserta.objects.create(nama=nama, email=email, acara=acara)
            acara.peserta_terdaftar += 1
            acara.save()
            return JsonResponse({'status': 'Pendaftaran berhasil'}, status=201)
        else:
            return JsonResponse({'status': 'Kapasitas penuh'}, status=400)
    return render(request, 'events/daftar_peserta.html', {'acara': acara})
