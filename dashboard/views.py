from django.shortcuts import render
from .models import Duyuru, Icerik

def anasayfa(request):
    duyurular = Duyuru.objects.all().order_by("-tarih")
    icerikler = Icerik.objects.all()
    return render(request, "base.html", {
        "duyurular": duyurular,
        "icerikler": icerikler,
    })