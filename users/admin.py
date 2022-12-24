from django.contrib import admin
from .models import Biodata
from .models import API
# Register your models here.


class BiodataAdmin(admin.ModelAdmin):
    list_display = ('user', 'alamat', 'telp')
admin.site.register(Biodata, BiodataAdmin)

class APIAdmin(admin.ModelAdmin):
    list_display = ('user', 'api_key')
admin.site.register(API, APIAdmin)
