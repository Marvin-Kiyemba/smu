from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile, User
from users.forms import CustomUserCreationForm, CustomUserChangeForm
from django.utils.translation import gettext as _
from assets.models import Asset
from records.models import Record
from .admin_inlines import UserProfileInline
from .models import DepartmentAdmin

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete=False
    verbose_plural_name="User Profile"
    fk_name = 'user'  

class CustomUserAdmin(UserAdmin):
    inlines =[UserProfileInline]
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display_links = ['email']
    search_fields = ('email',)
    ordering = ('email',)
    list_display = ('email', 'is_staff', 'is_active', 'is_superuser','department')
    list_filter = ('email', 'is_staff', 'is_active', 'is_superuser', 'user_type','department')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'user_type','department')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'is_staff', 'is_active', 'user_type','department')}
         ),
    )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

admin.site.register(User, CustomUserAdmin)
admin.site.register(DepartmentAdmin)

class AssetAdmin(admin.ModelAdmin):
    list_display = ('asset_type', 'asset_code','asset_model', 'purchase_value','date_added','status')
    list_filter = ('status', 'purchase_value')

admin.site.register(Asset, AssetAdmin)

class RecordAdmin(admin.ModelAdmin):
    list_display = ('asset_name', 'assigned_to', 'assigned_on', 'asset_status')
    list_filter = ('asset_status', 'assigned_to')

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'is_verified', 'created_at', 'updated_at')

admin.site.register(Record , RecordAdmin)
admin.site.register(UserProfile, UserProfileAdmin)