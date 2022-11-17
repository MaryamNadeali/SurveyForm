from django.shortcuts import render, redirect
from django.views import View
from .models import MulQuestion, TxtQuestion, MultipleAnswer, Answer
from .forms import FeedbackForm

# Create your views here.

class FeedbackFormView(View):
    
    def get(self, request):

        mul_que = MulQuestion.objects.all()
        multiple_anses = MultipleAnswer.objects.all()
        context = {
            'mul_que' : mul_que,
            'multiple_anses' : multiple_anses,
            }
        print(context)
        return render(request, 'question/que.html', context)
    
    def post(self, request, *args, **kwargs):
        print('bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb')
        form = FeedbackForm()
        questions = MulQuestion.objects.all()
        multiple_anses = MultipleAnswer.objects.all()
        if request.method == 'POST': 
            form = FeedbackForm(request.POST)
            if form.is_valid():
                print('wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww')
                bool_ans = form.cleaned_data.get('bool_ans')
                for question in questions:
                    if question.type == 'multianswer':
                        print('question',question)
                        multiple_anses = MultipleAnswer.objects.all().filter(que=question)
                        print('aaaaaaaaaaaaaaaaaaaaaa',multiple_anses)
                        for i in range(0,len(multiple_anses)):
                                answer = Answer.objects.create(que=question,ans=multiple_anses[i],bool_ans=bool_ans) 
                                answer.save()
                    else:
                        txt_ans = form.cleaned_data.get('txt_ans')
                        answer = Answer.objects.create(que=self.question,txt_ans=txt_ans)
                        answer.save()
                return redirect(request, 'question/end.html') 
            
            else:
                return render(request, 'question/que.html')           
                
        else:
            return render(request, 'question/que.html')
                    
        
