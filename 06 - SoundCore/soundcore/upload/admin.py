from django.contrib import admin
from upload.models import MusicList
from sorl.thumbnail.models import KVStore

# Register your models here.
admin.site.register(MusicList)
admin.site.register(KVStore)
