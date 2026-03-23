from django.contrib import admin
from .models import Skill

admin.site.register(Skill)
admin.site.site_header = 'Mayank Portfolio Admin'
admin.site.site_title = 'Portfolio Admin'
admin.site.index_title = 'Welcome to Dashboard'