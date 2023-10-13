from django import forms
from .models import Author

def validate_name(value):
    if len(value) < 2:
        raise forms.ValidationError('Name must have at least 2 characters')
    elif value == int:
        raise forms.ValidationError('Name must be a string')

def validate_surname(value):
    if len(value) < 2:
        raise forms.ValidationError('Name must have at least 2 characters')
    elif value == int:
        raise forms.ValidationError('Name must be a string')

def validate_patronymic(value):
    if len(value) < 2:
        raise forms.ValidationError('Name must have at least 2 characters')
    elif value == int:
        raise forms.ValidationError('Name must be a string')

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'surname', 'patronymic']

    name = forms.CharField(validators=[validate_name])
    surname = forms.CharField(validators=[validate_surname])
    patronymic = forms.CharField(validators=[validate_patronymic])
  

class RemoveAuthorsForm(forms.Form):
    authors_to_remove = forms.ModelMultipleChoiceField(queryset=Author.objects.filter(books=None), widget=forms.CheckboxSelectMultiple)
   
    


