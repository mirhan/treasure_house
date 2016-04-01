from django.contrib import admin
from west.models import Character,Contact,Tag

# Register your models here.
admin.site.register([Character, Contact, Tag])
