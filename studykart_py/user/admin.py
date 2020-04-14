from django.contrib import admin
from user.models import user_profile,user_roles,roles

# Register your models here.

admin.site.site_header = 'Studykart'

class user_profileAdmin(admin.ModelAdmin):
    list_display = ('user', 'created')
    list_filter = ('created',)

admin.site.register(user_profile, user_profileAdmin)
admin.site.register(user_roles)
admin.site.register(roles)