from django.contrib import admin
from .models import MulQuestion, TxtQuestion, MultipleAnswer, TxtAnswer, Answer

# Register your models here.
class MultiAnswerInline(admin.StackedInline):
    model = MultipleAnswer
    extra = 1
    
class QuestionAdmin(admin.ModelAdmin):
    inlines = [MultiAnswerInline]
    
admin.site.register(MulQuestion, QuestionAdmin)
admin.site.register(TxtQuestion)
admin.site.register(Answer)
admin.site.register(MultipleAnswer)
admin.site.register(TxtAnswer)
