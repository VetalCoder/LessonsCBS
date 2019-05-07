from django.db import models

# Create your models here.

class GoogleManager(models.Manager):
    def get_queryset(self):
        return super(GoogleManager, self).get_queryset().filter(company='google')

class ItvdnManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(company='itvdn')

class Human(models.Model):

    # choises
    CHOICE_COMPANY  = (
        ('google', 'Google'),
        ('yandex', 'Yandex'),
        ('itvdn', 'Itvdn'),
        ('epam', 'Epam'),
    )
    POSITION_CHOICES = (
        ('senior', 'Senior'),
        ('middle', 'Middle'),
        ('junior', 'Junior'),
    )
    LANGUAGE_CHOICES = (
        ('python', 'Python'),
        ('javascript', 'Javascript'),
        ('c#', 'C#'),
        ('cpp', 'C++'),
    )

    # fields
    name = models.CharField(max_length=50, verbose_name="Имя")
    surname = models.CharField(max_length=50, verbose_name="Фамилия")
    birth = models.DateField(auto_now_add=False, auto_now=False)
    company = models.CharField(max_length = 150, choices=CHOICE_COMPANY)
    position = models.CharField(max_length=15, choices=POSITION_CHOICES)
    language = models.CharField(max_length=10, choices= LANGUAGE_CHOICES, default='python')
    salary = models.IntegerField()

    #objects = models.Manager()
    #itvdn = ItvdnManager()
    #google = GoogleManager()

    def __str__(self):
        return 'Имя  - {0}, Фамилия -  {1}, Компания - {2}.'.format(self.name, self.surname, self.company)

    # to dictionary (lesson 8)
    def dict(self):
        obj = {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'birth': self.birth,
            'company': self.company,
            'position': self.position,
            'language': self.language,
            'salary': self.salary,
        }
        return obj