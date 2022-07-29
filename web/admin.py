from django.contrib import admin
from web.models import Post,Category


class PostAdmin(admin.ModelAdmin):
    list_display = ["id","author","title","category","date"]

admin.site.register(Post,PostAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id","name"]
    
admin.site.register(Category,CategoryAdmin)






