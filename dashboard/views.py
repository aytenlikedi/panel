from django.shortcuts import render, get_object_or_404
from .models import Duyuru

def anasayfa(request):
    duyurular = Duyuru.objects.all().order_by("-tarih")
    return render(request, "base.html", {"duyurular": duyurular})