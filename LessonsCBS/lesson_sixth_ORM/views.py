from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Human

# Create your views here.

# docs: https://docs.djangoproject.com/en/2.2/ref/models/querysets/#queryset-api
# field lookups docs: https://docs.djangoproject.com/en/2.2/ref/models/querysets/#field-lookups
class List(TemplateView):
    template_name = 'lesson_sixth_ORM/index.html'

    def get(self, request):
        # Human.objects.get(id=9).delete()
        all_humans = Human.objects.all() # Все сотрудники
        the_first_two = Human.objects.all()[:2]
        workers_google  = Human.objects.filter(company='google')
        filtered = Human.objects.filter(birth__year=1976) # сотрудники 1976 года рождения
        one_worker  = Human.objects.all()[0]
        ordered = Human.objects.all().order_by('-birth')
        sorted = Human.objects.filter(birth__year__lte=1980).order_by('birth')
        sorted_salary  = Human.objects.filter(salary__gte=1000, salary__lte=3000)
        name_vasya  = Human.objects.all().filter(name__contains='В')
        ctx = {
            'all_humans': all_humans,
            'workers_google': workers_google,
            'one_worker': one_worker,
            'filtered': filtered,
            'first_two': the_first_two,
            'ordered': ordered,
            'sorted': sorted,
            'sorted_salary': sorted_salary,
            'name_vasya' : name_vasya
        }
        return render(request , self.template_name , ctx)

    def post(self, request):
        query = request.POST['search']
        result_list  = Human.objects.filter(company=query)
        if result_list.count() != 0:
            context = {
                'result_list': result_list,
                'query': query,
            }
        else:
            context ={
                'empty': "Ничего не найдено :(",
                'query': query,
            }
        return render(request, 'lesson_sixth_ORM/result_search.html', context)