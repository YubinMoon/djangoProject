from django.contrib import admin
from bookmark.models import Bookmark

# 데코레이터 패턴을 사용하지 않는 방법
# admin.site.register(Bookmark)


@admin.register(Bookmark)
class BookMarkAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "url")
