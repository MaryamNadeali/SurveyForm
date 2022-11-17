from django.core.exceptions import ValidationError
from django import forms

def validate_txt_ans(self):
    for question in self.survey.question_set.all():

        if question.type == 'text':
            text_field = self.cleaned_data.get(f"question_{question.id}")
            list_sym=["!",">","<",";",":","@"]
            list_int=["0","1","2","3","4","5","6","7","8","9"]
            field_name = f"question_{question.id}"
            
            for int in list_int:
                if int in text_field:
                    raise forms.ValidationError({field_name:["Your answer Should not Contain Integers"]})
            for sym in list_sym:
                if sym in text_field:
                    raise forms.ValidationError({field_name:["Your answer Should not Contain Symboles"]})

    return text_field