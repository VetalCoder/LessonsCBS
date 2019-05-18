from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Author1)
admin.site.register(models.Article)
#admin.site.register(models.Cities)

class CitiesAdmin(admin.ModelAdmin):
    def get_all_authors(self, obj):
        #return "\n".join([p.products for p in obj.product.all()])
        authors = models.Author1.objects.all()
        return "; ".join([author.__str__() for author in authors if obj in author.city.all()])

    list_display = ("towns",'get_all_authors',)

admin.site.register(models.Cities, CitiesAdmin)