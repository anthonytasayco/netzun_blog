from django.contrib import admin
from .models import Publication
# Register your models here.

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    exclude = ['slug', ]