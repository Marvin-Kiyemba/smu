from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from assets.models import Asset
from django import forms

class SignUpForm(UserCreationForm):
    user_type = forms.ChoiceField(choices=User.USER_TYPE_CHOICES, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance.pk or self.instance.user_type == User.STAFF:
            del self.fields['user_type']
    
    class Meta(UserCreationForm):
        model = User
        fields = ('email','user_type')

    def clean_user_type(self):
        if self.instance.pk and self.instance.user_type == User.SUPER_USER:
            return self.instance.user_type
        user_type = self.cleaned_data['user_type']
        if not user_type and self.instance.pk:
            return self.instance.user_type
        return user_type

class CustomUserCreationForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email',)
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email',)

class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['asset_type', 'asset_code','asset_model','purchase_value','date_added']
        