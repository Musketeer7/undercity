from django.contrib import admin
from .views import File
from .models import Phrase
# Register your models here.

admin.site.register(File)
admin.site.register(Phrase)