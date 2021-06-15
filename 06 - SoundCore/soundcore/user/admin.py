from django.contrib import admin
from user.models import PasswordResetUrl, UserVolumeInput

# Register your models here.
admin.site.register(PasswordResetUrl)
admin.site.register(UserVolumeInput)
