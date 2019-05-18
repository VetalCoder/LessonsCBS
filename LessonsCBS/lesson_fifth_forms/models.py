from django.db import models

# Create your models here.

class Cities(models.Model):
    towns = models.CharField(max_length=200, blank=False, verbose_name="Город", help_text="Выберите городa со списка")

    def __str__(self):
        return f"Город -- {self.towns}"

class Author1(models.Model):

    CHOICES_FOR_CITY= (
        ('kyiv' , "Киев"),
        ('chernigov' , "Чернигов"),
        ('odessa' , "Одесса"),
        ('lvov' , "Львов"),
    )

    name = models.CharField(max_length=200, verbose_name="Имя автора")
    surname = models.CharField(max_length=200, verbose_name="Фамилия автора")
    city = models.ManyToManyField(Cities)



    def __str__(self):
        return f'Автор -- {self.name} {self.surname}'


class Article(models.Model):
    author = models.ForeignKey(Author1, verbose_name='Автор статьи', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    text = models.TextField(max_length=500, verbose_name="Текст статьи")

    def __str__(self):
        return f'Статья: {self.title}'