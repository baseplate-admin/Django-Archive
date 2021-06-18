from django.contrib import admin
from utility.models import UserVolumeInputCapture
from utility.models import UserPreviousSongCapture

# Register your models here.
admin.site.register(UserVolumeInputCapture)
admin.site.register(UserPreviousSongCapture)
