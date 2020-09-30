from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import site_conf

@login_required
def dashboard (request):
    nama_desa = site_conf.objects.filter(conf='desa').first()
    context = {
        'nama_desa': nama_desa.conf_val
    }
    return render(request, 'qapuas/dashboard.html', context)