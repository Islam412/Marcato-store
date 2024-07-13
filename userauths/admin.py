from django.contrib import admin
from userauths.models import User , Profile


class Profileadmin(admin.ModelAdmin):
    list_display = ('user','first_name','last_name','username','phone','address','city','country','verified')
    list_editable = ['verified']
    search_fields = ('first_name', 'last_name', 'username', 'phone', 'address', 'city', 'country')
    
class Useradmin(admin.ModelAdmin):
    list_display = ('email','first_name','last_name','username')

admin.site.register(User,Useradmin)
admin.site.register(Profile,Profileadmin)