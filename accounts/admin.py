from django.contrib import admin
from .models import Question, Answer, UserBestScore, Topic

# Register your models here.
admin.site.register(Question),
admin.site.register(Answer),
admin.site.register(UserBestScore),
admin.site.register(Topic),
