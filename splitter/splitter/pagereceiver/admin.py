from django.contrib import admin
from .views import File
from .models import Phrase, Known, KnownRepo
# Register your models here.

admin.site.register(File)
admin.site.register(Phrase)
admin.site.register(Known)
admin.site.register(KnownRepo)