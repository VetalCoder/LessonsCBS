from django.contrib import admin
from . import models

# Register your models here.

# admin.site.register(models.Example)

admin.site.register(models.Book)
admin.site.register(models.Place)
admin.site.register(models.Restaurant)
admin.site.register(models.Waiter)
admin.site.register(models.Publication)
admin.site.register(models.Article)


class ExampleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(models.Example, ExampleAdmin)


#class BookInline(admin.TabularInline):
#    model = models.Book
    
#class BookInline(admin.StackedInline):
#    model = models.Book

# docs: https://docs.djangoproject.com/en/2.2/ref/contrib/admin/#modeladmin-objects
class AuthorAdmin(admin.ModelAdmin):
    #list_display = ['name' , 'surname']
    list_display = [field.name for field in models.Author._meta.fields]
    #exclude = ["name"] #прячет поле
    #fields = ["name"] # показывает поле
    list_filter = ['name', 'surname']
    search_fields = ['name' , 'id']
    #search_fields = [field.name for field in models.Author._meta.fields]
    #inlines = [BookInline]
    class Meta:
        model = models.Author

admin.site.register(models.Author, AuthorAdmin)


#class PublicInline(admin.TabularInline):
#    model = models.Article.publications.through

#class PublicationAdmin(admin.ModelAdmin):
#    inlines = [
#        PublicInline,
#    ]

#class ArticleAdmin(admin.ModelAdmin):
#    inlines = [
#        PublicInline,
#    ]
#    exclude = ('publications',)

#admin.site.register(models.Publication, PublicationAdmin)
#admin.site.register(models.Article, ArticleAdmin)