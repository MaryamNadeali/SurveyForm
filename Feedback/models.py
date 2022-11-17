from django.db import models
from django.contrib.auth.models import User

class Survey(models.Model):
  STATUS = [
    ('pub','published'),
    ('un','unpublished')
  ]
  title = models.CharField(max_length=255)
  status = models.CharField(verbose_name='status', max_length=50, choices=STATUS)
  writer = models.ForeignKey(User, verbose_name="admin", on_delete=models.CASCADE)
  created_at = models.DateTimeField(verbose_name='creation_date', auto_now_add=True)
  updated_at = models.DateTimeField(verbose_name='updation_date', auto_now=True)

  def __str__(self):
    return self.title

class Question(models.Model):
  TYPE = [
    ('multianswer','multianswer'),
    ('text','text')
    ]
  type = models.CharField(verbose_name='type_question', max_length=50, choices=TYPE)
  survey = models.ForeignKey(Survey, on_delete=models.PROTECT)
  text = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')
  is_required = models.BooleanField(default=False)
  created_at = models.DateTimeField(verbose_name='creation_date', auto_now_add=True)
  updated_at = models.DateTimeField(verbose_name='updation_date', auto_now=True)

  def __str__(self):
    return self.text

class Choice(models.Model):
  question = models.ForeignKey(Question, null=True, on_delete=models.CASCADE)
  text = models.CharField(max_length=255)

  created_at = models.DateTimeField(verbose_name='creation_date', auto_now_add=True)
  updated_at = models.DateTimeField(verbose_name='updation_date', auto_now=True)

  def __str__(self):
    return f"{self.question.text}:{self.text}"

class Submission(models.Model):
  survey = models.ForeignKey(Survey, on_delete=models.PROTECT)
  tracking_code = models.CharField(verbose_name='tracking_code', max_length=20, null=True, blank=True)
  answer = models.ManyToManyField(Choice, blank=True)
  user = models.ForeignKey(User, verbose_name='user', on_delete=models.CASCADE)
  created_at = models.DateTimeField(verbose_name='creation_date', auto_now_add=True)
  updated_at = models.DateTimeField(verbose_name='updation_date', auto_now=True)


class TxtAnswer(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.PROTECT)
    que = models.ForeignKey(Question, verbose_name='question', on_delete=models.CASCADE, related_name='txtanswertoquestion')
    txt_ans =  models.TextField(verbose_name='text_answer', null=True, blank=True)
    user = models.ForeignKey(User, verbose_name='user', on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name='creation_date', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='updation_date', auto_now=True)
    
    def __str__(self):
        return self.que.text
