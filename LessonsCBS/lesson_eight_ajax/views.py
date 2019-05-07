from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from .forms import HumanForm, UserCreateForm
from lesson_sixth_ORM.models import Human
from django.contrib.auth.models import User

from django.http import HttpResponseRedirect , HttpResponse , JsonResponse

from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.

# docs: https://docs.djangoproject.com/en/2.2/topics/auth/#user-authentication-in-django
# docs: https://docs.djangoproject.com/en/2.2/topics/auth/default/#using-the-django-authentication-system
class MainView(TemplateView):
    template_name = 'lesson_eight_ajax/ajax.html'
    human_form = HumanForm
    def get(self, request):
        ctx = {}
        if request.user.is_authenticated:
            all_humans  = Human.objects.all()
            ctx['humans'] = all_humans
            ctx['human_form'] = self.human_form
        return render(request, self.template_name, ctx)


class RegisterFormView(FormView):
    form_class = UserCreateForm
    success_url = reverse_lazy("lesson_eight_ajax:login")
    template_name = "lesson_eight_ajax/registration.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterFormView, self).form_invalid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm

    # Аналогично регистрации, только используем шаблон аутентификации.
    template_name = "lesson_eight_ajax/login.html"

    # В случае успеха перенаправим на главную.
    success_url = reverse_lazy('lesson_eight_ajax:main')

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()

        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(LoginFormView, self).form_valid(form)
    

class LogoutView(TemplateView):
    def get(self, request):
        logout(request)

        # После чего, перенаправляем пользователя на главную страницу.
        return redirect("lesson_eight_ajax:main")


# Handlers
def validate_email(request):
    if request.GET:
        email = request.GET.get('email')
        is_taken = User.objects.filter(email=email).exists()
        if is_taken:
            data  = {
                "is_taken" : "На этот почтовый ящик уже зарегистрирован пользователь!"
            }
            return JsonResponse(data)
        else:
            return JsonResponse({'ok': "На этот почтовый адрес не было регистраций"})

def show_three(request):
    first_three = Human.objects.all()[:3].values()
    context  = {
        'elements' : list(first_three)
    }
    return JsonResponse(context)

def show_four(request):
    first_four = Human.objects.all()[:4].values()
    context = {
        'elements': list(first_four)
    }
    return JsonResponse(context)

def add_human(request):
    if request.POST:
        if request.is_ajax():
            name = request.POST['name']
            surname = request.POST['surname']
            birth = request.POST['birth']
            company = request.POST['company']
            position = request.POST['position']
            language = request.POST['language']
            salary = request.POST['salary']
            human = Human.objects.create(name=name,
                                 surname=surname,
                                 birth=birth,
                                 company=company,
                                 position=position,
                                 language=language,
                                 salary=salary
                                 )
            return JsonResponse(human.dict())