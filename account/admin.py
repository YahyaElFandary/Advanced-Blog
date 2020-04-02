from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin

class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name','data_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'username',)
    readonly_fields = ('data_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)
