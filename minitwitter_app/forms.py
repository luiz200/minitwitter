from django import forms
from .models import public
from captcha.fields import CaptchaField

class publicForm(forms.ModelForm):

    class Meta:
        model = public
        fields = ['title', 'text', 'file']

class CaptchaForm(forms.Form):
    captcha = CaptchaField()


