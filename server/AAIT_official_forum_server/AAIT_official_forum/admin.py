from django.contrib import admin
from AAIT_official_forum.models import User,Administrator,Article,ArticleBoard,ArticleComment,Goods,PoromodoClock
# Register your models here.

admin.site.register(User)
admin.site.register(Article)
admin.site.register(Goods)
admin.site.register(PoromodoClock)