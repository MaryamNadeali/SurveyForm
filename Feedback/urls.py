from django.urls import path
from .views import FeedbackFormView

app_name = 'Feedback'

urlpatterns = [
    path("", FeedbackFormView.as_view(), name='que'),
]
