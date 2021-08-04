from django.contrib import admin
from questions.models import Question


class QuestAdmin(admin.ModelAdmin):
    field = ['question', 'contact']


admin.site.register(Question, QuestAdmin)
