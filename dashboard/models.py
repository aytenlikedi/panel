from django.db import models

class Duyuru(models.Model):
    baslik = models.CharField(max_length=200)
    icerik = models.TextField()
    kapak = models.ImageField(upload_to='kapaklar/', null=True, blank=True)
    tarih = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.baslik
    
class Icerik(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='icerikler/', null=True, blank=True)
    url = models.CharField(max_length=500, null=True, blank=True)
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title