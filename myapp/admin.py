from django.contrib import admin
from . models import Ins_Mark
from . models import Qna

# Register your models here.
admin.site.register(Ins_Mark)
admin.site.register(Qna)
admin.site.site_header = 'SoftWaves Admin'
admin.site.index_title = 'Welcome to SoftWaves Portal'