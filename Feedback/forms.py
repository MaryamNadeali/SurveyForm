from django import forms
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Submission, Choice, TxtAnswer, Question, Survey
from .validate import validate_txt_ans
from .utils import trackingCode

#==========================================================RegisterForm======================================================

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password']

#==========================================================LoginForm=========================================================

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']

#==========================================================SurveyForm========================================================

class SurveyForm(forms.Form):
    question_1 = forms.ChoiceField(widget=forms.RadioSelect, choices=())

    def __init__(self, survey, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.survey = survey
        del self.fields["question_1"]
        for question in survey.question_set.all():
            print(question.type)
            if question.type == 'multianswer':
                choices = [(choice.id, choice.text) for choice in question.choice_set.all()]
                self.fields[f"question_{question.id}"] = forms.ChoiceField(widget=forms.RadioSelect, choices=choices)

                if question.is_required == False:
                    self.fields[f"question_{question.id}"].required = False
                self.fields[f"question_{question.id}"].widget.attrs.update({'class': 'form-check-input'})
                self.fields[f"question_{question.id}"].label = question.text
                self.fields[f"question_{question.id}"].widget.attrs.update({'class': 'feedback_title'})

            else:
                self.fields[f"question_{question.id}"] = forms.CharField(widget=forms.Textarea)
                if question.is_required == False:
                    self.fields[f"question_{question.id}"].required = False
                self.fields[f"question_{question.id}"].widget.attrs.update({'class': 'form-control'})
                self.fields[f"question_{question.id}"].label = question.text
                self.fields[f"question_{question.id}"].widget.attrs.update({'class': 'form-group mb-2 col-12'})

    def clean(self):
        super(SurveyForm, self).clean()
        validate_txt_ans(self)
        return self.cleaned_data

    def save(self, **kwargs):
        data = self.cleaned_data
        user = kwargs.pop('user')
        tracking_code = trackingCode()
        submission = Submission(survey=self.survey,user=user, tracking_code=tracking_code)
        submission.save()
        for question in self.survey.question_set.all():
            if question.type == 'multianswer':
                try:
                    # choice = Choice.objects.get(pk=data[f"question_{question.id}"])
                    choice = get_object_or_404(Choice,pk=data[f"question_{question.id}"])
                    submission.answer.add(choice)
                except:
                    submission.save()
            else:
                question = Question.objects.get(id=question.id)
                txtanswer = TxtAnswer(survey=self.survey,que=question,txt_ans=data[f"question_{question.id}"],user=user)
                txtanswer.save()
        submission.save()
        txtanswer.save()
        return submission, txtanswer

