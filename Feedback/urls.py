from django.urls import path
from . import views

app_name='feedback'

urlpatterns = [
    path('register/',views.RegisterView.as_view(), name="register"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('', views.SelectSurveyView.as_view(), name="feedbacks"),
    path("survey/<int:id>/", views.show_survey, name="show-survey"),
    path("end/", views.DisplayCodeView.as_view(), name="end")
]


