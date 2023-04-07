from django.contrib import admin

from users.models import EmailVerification, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'username')


@admin.register(EmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_code')
