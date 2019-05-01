from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from django.views import generic

# Create your views here.

# request methods and properties.... this is beginning)
# docs: https://docs.djangoproject.com/en/2.2/ref/request-response/#httprequest-objects
def test_view(request):
    test_string = f"""
        <div>WELCOME TO: {request.path}</ div>
        <div>HOST IS: {request.get_host()}</ div>
        <div>FULL PATH IS: {request.get_full_path()}</ div>
        <div>PROTECTED: {request.is_secure()}</ div>
        <div>METHOD: {request.method}</ div>
        <div>USER: {request.user}</ div>
        <div>HEADERS: {request.headers}</ div>
    """
    return  HttpResponse(test_string)


# html form (and handlers)
# docs: https://docs.djangoproject.com/en/2.2/topics/forms/#html-forms
def show_html_form(request):
    return render(request, "lesson_fifth_forms/html_form.html")

def search(request):
    if request.method == "GET":
        if 'search-word' in request.GET:
            return HttpResponse("Вы хотели найти {}".format(request.GET['search-word']))
        else:
            return HttpResponse("Вы отправили пустую форму")

def file_input(request):
    if request.method == "POST":
        name = request.POST['name']
        surname = request.POST['surname']
        birth = request.POST['birth']
        gender = request.POST['gender']

        some_file = open("some.txt", "w")
        some_file.write("Имя :" + name + "\n")
        some_file.write("Фамилия :" + surname + "\n")
        some_file.write("Дата рождения :" + birth + "\n")
        some_file.write("Пол :" + gender + "\n")
        some_file.close()
    return HttpResponse("Данные успешно были записаны!")


# model forms (and handlers)
# docs: https://docs.djangoproject.com/en/2.2/topics/forms/modelforms/#modelform
def show_model_form(request):
    form_for_author1 = forms.AuthorOneForm
    form_for_article = forms.ArticleForm
    context = {
        'form_for_author1' : form_for_author1,
        'form_for_article' : form_for_article,
    }
    return render(request, 'lesson_fifth_forms/model_forms_and_Form.html', context)

def add_author(request):
    form = forms.AuthorOneForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            data = form.cleaned_data
            form.save()
            print(data)
            return HttpResponse(f"Автор добавлен!")

def add_article(request):
    form = forms.ArticleForm(request.POST)
    if request.method == "POST" and form.is_valid():
        form = form.save()
        return HttpResponse("Статья добавлена!")


# form, basis on class Form (with using class-view)
# docs: https://docs.djangoproject.com/en/2.2/topics/forms/#the-form-class
class ContactFormView(generic.TemplateView):
    form_contact  = forms.ContactForm

    def post(self, request):
        form = forms.ContactForm(request.POST)
        context = {
            'form_contact': form,
        }
        if form.is_valid():
            data = form.cleaned_data
            return HttpResponse(f"We received: {data.items()}")
        else:
            return render(request, 'lesson_fifth_forms/model_forms_and_Form.html', context)

    def get(self, request):
        context = {
            'form_contact' : self.form_contact
        }
        return render(request, 'lesson_fifth_forms/model_forms_and_Form.html', context)


# validators
# docs: https://docs.djangoproject.com/en/2.2/ref/validators/#module-django.core.validators
class UrlView(generic.TemplateView):
    form_submit_url = forms.UrlForm

    def get(self , request):
        context  = {
            'form_url': self.form_submit_url
        }
        return render(request, 'lesson_fifth_forms/url_form_validate.html', context)

    def post(self , request):
        form  = forms.UrlForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            print(data)
        else:
            print('invalid')
            context = {
                'form_url': form
            }
            return render(request, 'lesson_fifth_forms/url_form_validate.html', context)
        return HttpResponse(f"Data received: {form.cleaned_data.items()}")