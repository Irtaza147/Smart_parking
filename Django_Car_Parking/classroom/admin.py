from django.contrib import admin
from django.contrib.auth.models import User
from .models import ImageUploadForm

# Register your models here.
#admin.site.register(User)
admin.site.register(User)  # Register the User model
@admin.register(ImageUploadForm)
class Image(admin.ModelAdmin):
    list_display=['id','date','image']