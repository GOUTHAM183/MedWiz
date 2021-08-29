from django.contrib import admin
from .models import Post,Update,Medicine,Customer

# Register your models here.
admin.site.register(Post)
admin.site.register(Update)
admin.site.register(Medicine)
admin.site.register(Customer)
