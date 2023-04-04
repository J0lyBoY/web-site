from .models import News
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'data', 'short_text', 'full_text', ]

        widgets = {
            'title': TextInput(attrs={
                'class': "form-control",
                'placeholder': "Название статьи",
            }),
            'data': DateTimeInput(attrs={
                'class': "form-control",
                'placeholder': "Дата публикации",
            }),
            'short_text': TextInput(attrs={
                'class': "form-control",
                'placeholder': "Краткое описание статьи",
            }),
            'full_text': Textarea(attrs={
                'class': "form-control",
                'placeholder': "Полный текст статьи",
            }),
        }
