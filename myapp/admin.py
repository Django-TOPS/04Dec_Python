from django.contrib import admin
from .models import signup

# Register your models here.
class signupAdmin(admin.ModelAdmin):
    list_display=['id','fname','lname','username','password','city','state','zipcode']
        

admin.site.register(signup,signupAdmin)