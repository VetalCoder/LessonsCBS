from django import forms
from . import models
from django.core.validators import URLValidator, ValidationError

# forms, basis on models
class AuthorOneForm(forms.ModelForm):
    class Meta:
        model = models.Author1
        fields = ['name', 'surname', 'city']
        #widgets = {
        #    'city' : forms.SelectMultiple()
        #    #'name': Textarea(attrs={'cols': 80, 'rows': 20}),
        #}


class ArticleForm(forms.ModelForm):
    class Meta:
        model = models.Article
        fields  = ['author', 'title', 'text']

# form, basis on class Form
class ContactForm(forms.Form):
    LANGUAGE_CHOICES = (
        ('python', 'Python'),
        ('javascript', 'Javascript'),
        ('c#', 'C#'),
        ('cpp', 'C++'),
        ('scala', 'Scala'),
        ('lisp', 'Lisp'),
        ('java', 'Java'),
        ('lua', 'Lua'),
        ('typescript', 'Typescript'),
        ('go', 'Go'),
        ('prolog', 'Prolog'),
        ('swift', 'Swift'),
        ('ada', 'Ada'),
        ('coffeescript', 'Coffeescript'),
        ('c', 'C'),
    )

    lang = forms.MultipleChoiceField(choices=LANGUAGE_CHOICES)

    boolean_field = forms.NullBooleanField()
    float_field = forms.FloatField()
    name_sender = forms.CharField(max_length=100, label="Введите ваше имя")
    message = forms.CharField(widget=forms.Textarea, label="Сообщение")
    sender = forms.EmailField(label="Введите ваш емейл!")


# form with validators
def validate_url(value):
    validation_url = URLValidator()
    value_one_invalid = False
    value_two_invalid = False
    try:
        validation_url(value)
    except:
        value_one_invalid = True

    value_two_url  = 'http://' + value
    try:
        validation_url(value_two_url)
    except:
        value_two_invalid = True

    if value_one_invalid == True and value_two_invalid == True:
        raise ValidationError("Неправильный адрес сайта!")

def check_dot_com(value):
    if not '.com' in value:
        raise ValidationError("Адрес сайта не содержит '.com'!")

def check_itvdn(value):
    if not 'itvdn' in value:
        raise ValidationError("Это не сайт ITVDN!")

# form
class UrlForm(forms.Form):
    title  = forms.CharField(label='Название сайта')
    url = forms.CharField(label='Адрес сайта', validators=[validate_url, check_dot_com, check_itvdn])
    #url = forms.CharField(label='Адрес сайта', validators=[URLValidator()])            # default validator


    # Another way, not recommended
    #def clean(self):
    #    cleaned_data = super(UrlForm , self).clean()
    
    #def clean_url(self):
    #    url = self.cleaned_data['url']
    #    validation_url  = URLValidator()
    #    try:
    #        validation_url(url)
    #    except:
    #        raise forms.ValidationError('Это не адрес сайта!')
    #    return url
