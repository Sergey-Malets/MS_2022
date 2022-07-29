from django.contrib import admin
from .models import Post, Category


#вы определяете пустые классы PostAdmin и CategoryAdmin.
# Для целей данного руководства вам не нужно добавлять какие-либо атрибуты или методы в эти классы.
# Они используются для настройки того, что показано на страницах администратора.
class PostAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post,PostAdmin)
admin.site.register(Category, CategoryAdmin)
