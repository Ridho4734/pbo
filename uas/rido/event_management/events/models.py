from django.db import models

class Acara(models.Model):
    judul = models.CharField(max_length=200)
    deskripsi = models.TextField()
    tanggal = models.DateField()
    lokasi = models.CharField(max_length=200)
    kapasitas = models.IntegerField()
    peserta_terdaftar = models.IntegerField(default=0)

    def __str__(self):
        return self.judul

class Peserta(models.Model):
    nama = models.CharField(max_length=200)
    email = models.EmailField()
    acara = models.ForeignKey(Acara, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama
