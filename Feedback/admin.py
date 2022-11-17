from django.contrib import admin
from django.apps import apps
from .models import Survey, Question, Choice, Submission, TxtAnswer

class QuestionInline(admin.TabularInline):
  model = Question
  show_change_link = True

class ChoiceInline(admin.TabularInline):
  model = Choice


class SurveyAdmin(admin.ModelAdmin):
  inlines = [
    QuestionInline
  ]

class QuestionAdmin(admin.ModelAdmin):
  inlines = [
    ChoiceInline
  ]

# @admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    readonly_fields = ['user']

# @admin.register(TxtAnswer)
class TxtAnswerAdmin(admin.ModelAdmin):
    readonly_fields = ['user']
  
# class SubmissionAdmin(admin.ModelAdmin):
#   list_display = ('status')

# app_config = apps.get_app_config('feedback')
# models = app_config.get_models()

# for model in models:
#     try:
#         admin.site.register(model)
#     except admin.sites.AlreadyRegistered:
#         pass

admin.site.register(Survey, SurveyAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission, SubmissionAdmin)
admin.site.register(TxtAnswer, TxtAnswerAdmin)
