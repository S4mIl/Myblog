from django.contrib import admin
from .models import Tag,Blog,Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}


admin.site.register(Tag,TagAdmin)
admin.site.register(Blog)
admin.site.register(Category,CategoryAdmin)
