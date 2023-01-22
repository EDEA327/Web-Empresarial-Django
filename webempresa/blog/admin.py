from django.contrib import admin
from .models import Category,Post

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields =('created_at','updated_at')

class PostAdmin(admin.ModelAdmin):
    readonly_fields =('created_at','updated_at')
    list_display = ('title','author','published','post_categories')
    ordering = ('author','published')
    search_fields = ('title','content','author__username','categories__name')
    date_hierarchy = 'published'
    list_filter = ('author__username','categories__name')

    def post_categories(self,obj):
        #! Se está devolviendo el nombre de las categorias a las que pertenece
        #! el objeto (obj)
        return ", ".join([c.name for c in obj.categories.all().order_by('name')])
    post_categories.short_description = 'Categorias'

# Registros
admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)
