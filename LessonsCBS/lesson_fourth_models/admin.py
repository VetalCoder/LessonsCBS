from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Example)
admin.site.register(models.Book)
admin.site.register(models.Place)
admin.site.register(models.Restaurant)
admin.site.register(models.Waiter)
admin.site.register(models.Publication)
admin.site.register(models.Article)


####### for slug-field
#class ExampleAdmin(admin.ModelAdmin):
#    prepopulated_fields = {"slug": ("title",)}

#admin.site.register(models.Example, ExampleAdmin)



####### Inline Book

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



######## Inline ManyToMany

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



# Adding actions (to Book for example)
# docs: https://docs.djangoproject.com/en/2.2/ref/contrib/admin/actions/#writing-actions

#class BookAdmin(admin.ModelAdmin):
#    list_display = ['title', 'status']
#    ordering = ['title']
#    actions = ['make_published']

#    def make_published(self, request, queryset):
#        rows_updated = queryset.update(status='p')
#        if rows_updated == 1:
#            message_bit = "1 story was"
#        else:
#            message_bit = "%s stories were" % rows_updated
#        self.message_user(request, "%s successfully marked as published." % message_bit)
#    make_published.short_description = "Mark selected stories as published"

#admin.site.register(models.Book, BookAdmin)