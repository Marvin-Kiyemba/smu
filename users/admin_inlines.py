from django.contrib import admin
from users.models import UserProfile


class UserProfileInline(admin.StackedInline):
     model = UserProfile
     can_delete = False
     verbose_plural_name = "User Profile"
     fk_name = "user"
