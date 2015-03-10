from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from account.forms import AccountCreationForm, AccountChangeForm
from account.models import Account


class AccountAdmin(UserAdmin):
    form = AccountChangeForm
    add_form = AccountCreationForm

    list_display = ('username', 'email', 'is_staff', 'is_superuser')
    list_filter = ('is_superuser',)

    fieldsets = (
        ('Account', {'fields': ('username', 'email', 'password', 'first_name', 'last_name', 'photo', 'biography')}),
        ('Permission', {'fields': ('is_active', 'is_superuser', 'is_staff')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_superuser')
        }),
    )
    search_fields = ('username', 'email')
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)


admin.site.register(Account, AccountAdmin)

