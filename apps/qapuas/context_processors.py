from .models import site_conf

def Qconf(request):
    nama_desa = site_conf.objects.filter(conf='desa').first()
    kecamatan = site_conf.objects.filter(conf='kec').first()
    kabupaten = site_conf.objects.filter(conf='kab').first()
    kode_desa = site_conf.objects.filter(conf='kode').first()

    return {
        'conf_nama_desa': nama_desa.conf_val,
        'conf_kec': kecamatan.conf_val,
        'conf_kab': kabupaten.conf_val,
        'conf_kode_desa': kode_desa.conf_val
    }
