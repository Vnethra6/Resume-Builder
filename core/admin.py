from django.contrib import admin
from .models import Basic_info, Education, Experience, Skills, Interest
# Register your models here.

admin.site.register(Basic_info)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Skills)
admin.site.register(Interest)