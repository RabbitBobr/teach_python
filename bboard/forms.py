from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField

from .models import Bb, Rubric



class BbForm(forms.ModelForm):
    title = forms.CharField(label='Название товара', validators=[validators.RegexValidator(regex='^.{4,}$')],
                            error_messages={'invalid': 'Короткое название'})
    price = forms.DecimalField(label='Цена', decimal_places=2)
    rubric = forms.ModelChoiceField(queryset=Rubric.objects.all(), label='Рубрика',
                                    help_text='Не забудте про рубрику', widget=forms.widgets.Select(attrs={'size': 8}))

    def clean(self):
        super().clean()
        errors = {}
        if not self.cleaned_data['content']:
            errors['content'] = ValidationError('Укажите описание')
        if self.cleaned_data['price'] < 0:
            errors['price'] = ValidationError('Цена не может быть отрицательной')
        if errors:
            raise ValidationError(errors)

    class Meta:
        model = Bb
        fields = ('title', 'content', 'price', 'rubric')
        labels = {'title': 'Название товара'}


class SearchForm(forms.Form):
    keyword = forms.CharField(max_length=20, label='Искомое слово')
    rubric = forms.ModelChoiceField(queryset=Rubric.objects.all(), label='Рубрика')

