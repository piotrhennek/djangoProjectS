from django.contrib import admin
from . import models

class TemplateAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'description', 'date_creation')

class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'doc_id')

# Register your models here.
admin.site.register(models.Template, TemplateAdmin)
admin.site.register(models.Tag, TagAdmin)
