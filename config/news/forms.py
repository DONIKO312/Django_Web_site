from django import forms
from .models import News

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'anons', 'full_text', 'date', 'image']  # Добавлено поле image

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            'anons': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс'
            }),
            'date': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата статьи'
            }),
            'full_text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control-file'  # Используйте form-control-file для загрузки файлов
            })
        }
