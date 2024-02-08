from django.contrib import admin
from account.models import CustomUser, PasswordResetToken

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(PasswordResetToken)
