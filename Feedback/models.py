from email.policy import default
from enum import unique
from random import choices
from tabnanny import verbose
from xmlrpc.client import boolean
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MulQuestion(models.Model):
    
    TYPE = [
        ('multianswer','multianswer'),
        ('text','text')
    ]
    type = models.CharField(verbose_name='type_question', max_length=50, choices=TYPE)
    title = models.CharField(verbose_name='title', max_length=100, unique=True)
    question = models.CharField(verbose_name='question_text', max_length=100)
    writer = models.ForeignKey(User, verbose_name='writer', on_delete=models.CASCADE, related_name='questiontouser')
    created_at = models.DateTimeField(verbose_name='creation_date', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='updated_date', auto_now=True)
    
    def __str__(self):
        return self.title
        
    class Meta:
        db_table = 'question'
        
class MultipleAnswer(models.Model):
    
    txt_ans =  models.CharField(verbose_name='txt_ans', max_length=100)
    boolean_ans = models.BooleanField(default=False)
    writer = models.ForeignKey(User, verbose_name='writer', on_delete=models.CASCADE, related_name='mulanswertouser')
    que = models.ForeignKey(MulQuestion, verbose_name='question', on_delete=models.CASCADE, related_name='mulanswertoquestion')
    created_at = models.DateTimeField(verbose_name='creation_date', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='updation_date', auto_now=True)
    is_active = models.BooleanField(verbose_name='activation_option', default=True)
    
    def __str__(self):
        return self.txt_ans
        
    class Meta:
        db_table = 'option'
        
class TxtQuestion(models.Model):
    
    TYPE = [
        ('multianswer','multianswer'),
        ('text','text')
    ]
    type = models.CharField(verbose_name='type_question', max_length=50, choices=TYPE)
    title = models.CharField(verbose_name='title', max_length=100, unique=True)
    question = models.CharField(verbose_name='question_text', max_length=100)
    writer = models.ForeignKey(User, verbose_name='writer', on_delete=models.CASCADE, related_name='txtquestiontouser')
    created_at = models.DateTimeField(verbose_name='creation_date', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='updated_date', auto_now=True)
    
    def __str__(self):
        return self.title
        
    class Meta:
        db_table = 'txt_que'
        
class TxtAnswer(models.Model):
    
    txt_ans =  models.TextField(verbose_name='text_answer')
    writer = models.ForeignKey(User, verbose_name='writer', on_delete=models.CASCADE, related_name='txtanswertouser')
    que = models.OneToOneField(TxtQuestion, verbose_name='question', on_delete=models.CASCADE, related_name='txtanswertoquestion')
    created_at = models.DateTimeField(verbose_name='creation_date', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='updation_date', auto_now=True)
    
    def __str__(self):
        return self.que.txt_ans
        
    class Meta:
        db_table = 'txt_ans'
        
# class AnswerManager(models.Manager):
#     def get_queryset(self):
#         questions = MulQuestion.objects.all()
#         for question in questions:
#             if question.type == 'multianswer':
#                 print('question',question)
#                 # multiple_anses = MultipleAnswer.objects.all().filter(que=question)
#         return MultipleAnswer.objects.all().filter(que=question)
        
class Answer(models.Model):
    # user = models.ForeignKey(User, verbose_name='user', on_delete=models.CASCADE)
    que = models.ForeignKey(MulQuestion, verbose_name='que', on_delete=models.CASCADE)
    ans = models.ForeignKey(MultipleAnswer, verbose_name='ans', on_delete=models.CASCADE)
    bool_ans = models.BooleanField(default=False)
    txt_ans =  models.TextField(verbose_name='text_answer')
    created_at = models.DateTimeField(verbose_name='creation_date', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='updation_date', auto_now=True)
    
    

    
