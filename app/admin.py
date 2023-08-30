from django.contrib import admin
from .models import NameModel

class NamePanel ( admin.ModelAdmin ) : 
    list_display = ['name','updated_at']

admin.site.register(NameModel,NamePanel)
