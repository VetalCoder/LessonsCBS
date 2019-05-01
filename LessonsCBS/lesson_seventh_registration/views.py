from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.views.generic.edit import FormView
from lesson_sixth_ORM.models import Human
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# my form
from .forms import UserCreateForm, ProfileEditForm
from .models import Profile

# Create your views here.

class MainView(TemplateView):
    template_name = 'lesson_seventh_registration/main_page.html'

    def get(self, request):
        if request.user.is_authenticated:
            humans = Human.objects.all()
            ctx = {}
            ctx['humans'] = humans
            return render(request, self.template_name, ctx)
        else:
            return render(request, self.template_name, {})


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "lesson_seventh_registration/login.html"
    success_url = "/lesson-seventh/"

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()

        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class RegisterFormView(FormView):
    form_class = UserCreationForm
    
    # my form
    #form_class = UserCreateForm

    success_url = "/lesson-seventh/login"
    template_name = "lesson_seventh_registration/registration.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterFormView, self).form_invalid(form)


# advanced register
class AdvansedRegisterFormView(TemplateView):
    template_name = 'lesson_seventh_registration/registration_advansed.html'
    main_form = UserCreateForm
    add_form = ProfileEditForm

    def get(self, request):
        context = {
            'main_form': self.main_form,
            'add_form': self.add_form,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        print(request.POST)
        main_form = UserCreateForm(request.POST)
        add_form = ProfileEditForm(request.POST)
        if main_form.is_valid() and add_form.is_valid():
            # Create a new user object and saving it
            new_user = main_form.save()

            # Create profile object
            profile = Profile.objects.create(user=new_user, biography=add_form.cleaned_data["biography"],
                                             birth_date=add_form.cleaned_data["birth_date"])
            return HttpResponseRedirect('/lesson-seventh/login')
        else:
            return render(request, self.template_name, {'main_form': main_form, "add_form": add_form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/lesson-seventh/")