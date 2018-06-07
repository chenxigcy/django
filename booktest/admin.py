from django.contrib import admin
from booktest.models import BookInfo,HeroInfo

# Register your models here.
class HeroInfoInline(admin.StackedInline):
    extra = 2
    model = HeroInfo

class BookInfoAdmin(admin.ModelAdmin):
    search_fields = ['btitle']
    list_display = ['pk','btitle','bpub_date']
    inlines = [HeroInfoInline]

admin.site.register(BookInfo,BookInfoAdmin)