from django.views import View
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .models import Survey,Submission
from .forms import RegisterForm, LoginForm, SurveyForm

#==================================================RegisterView=============================================

class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request,'account/register.html',{'register_form':register_form})

    def post(self, request):
        register_form = RegisterForm()
        if request.method == 'POST':
            register_form = RegisterForm(request.POST)
            if register_form.is_valid():
                user = register_form.save()
                user.set_password(user.password)
                user.save()
                messages.success(request,'ثبت اطلاعات با موفقیت انجام شد')
                return redirect('feedback:login')
            else:
                messages.error(request, 'اطلاعات وارد شده معتبر نمی باشد')
                return render(request, 'account/register.html', {'register_form': register_form})

        else:
            messages.error(request, 'اطلاعات وارد شده معتبر نمی باشد')
            return render(request, 'account/register.html', {'register_form': register_form})

#==================================================LoginView================================================

class LoginView(View):
    def get(self,request):
        login_form = LoginForm()
        return render(request, 'account/login.html', {'login_form':login_form})

    def post(self, request):
        login_form = LoginForm()
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('feedback:feedbacks')
        else:
            messages.warning(request,'کاربر با این مشخصات یافت نشد')
            return render(request, 'account/login.html', {'login_form':login_form})

#===============================================SelectSurveyView===========================================

class SelectSurveyView(View):

    def get(self, request):
        feedbacks = Survey.objects.all().filter(status='pub')
        context = {
            'feedbacks': feedbacks,
        }

        return render(request, 'account/select_survey.html',context)


#==================================================Surveyview===============================================
def index(request):
    return render(request, "lewagon/index.html")

def show_survey(request, id=None):
    survey = get_object_or_404(Survey, pk=id)
    user = request.user
    # if submission is None:
    post_data = request.POST if request.method == "POST" else None
    form = SurveyForm(survey, post_data)

    url = reverse("show-survey", args=(id,))
    if form.is_bound and form.is_valid():
        form.save(user=request.user, commit=False)
        submission = Submission.objects.all().last()
        tracking_code = submission.tracking_code
        messages.add_message(request, messages.INFO, 'Submissions saved. \n Your Tracking Code is %s' %tracking_code, extra_tags='success')
        # messages.add_message(request, messages.INFO, 'Your Tracking Code is %s' %tracking_code, extra_tags='tracking_code')
        return redirect(url)

    else:
        context = {
        "survey": survey,
        "form": form,
        }
        return render(request, "feedback/survey.html", context)
    # else:
    #     context = {
    #         "survey": survey,
    #         }
    #     messages.add_message(request, messages.INFO, 'You fielled this form before.')
    #     return render(request, "feedback/survey.html", context)


#=======================================================SaveFormAndDisplayCodeView=====================================================

class DisplayCodeView(View):

    def get(self, request):
        submission = Submission.objects.all().last()
        tracking_code = submission.tracking_code
        context = {
            'tracking_code': tracking_code,

        }
        return render(request, 'feedback/end.html', context)
