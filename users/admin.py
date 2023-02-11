from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile, User
from users.forms import CustomUserCreationForm, CustomUserChangeForm
from django.utils.translation import gettext as _
from assets.models import Asset
from records.models import Record

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete=False
    verbose_plural_name="User Profile"
    fk_name = 'user'  

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display_links = ['email']
    search_fields = ('email',)
    ordering = ('email',)
    # inlines = (UserProfileInline,)
    list_display = ('email', 'is_staff', 'is_active', 'is_superuser',)
    list_filter = ('email', 'is_staff', 'is_active', 'is_superuser', 'user_type')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email','user_type')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'user_type')}
         ),
    )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

admin.site.register(User, CustomUserAdmin)


class AssetAdmin(admin.ModelAdmin):
    list_display = ('asset_type', 'asset_code','asset_model', 'purchase_value','date_added','status')
    list_filter = ('status', 'purchase_value')

admin.site.register(Asset, AssetAdmin)

class RecordAdmin(admin.ModelAdmin):
    list_display = ('asset_name', 'assigned_to', 'assigned_on', 'asset_status')
    list_filter = ('asset_status', 'assigned_to')

admin.site.register(Record , RecordAdmin)