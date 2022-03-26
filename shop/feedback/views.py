from django.views.generic.edit import FormView
from feedback.forms import FeedbackForm
from django.views.generic.edit import CreateView
from feedback.models import Feedback


class FeedbackView(FormView):
    template_name = 'feedback/feedback_form.html'
    form_class = FeedbackForm
    success_url = 'feedback/create'


class FeedbackCreateView(CreateView):
    model = Feedback
    fields = ['user_name', 'email', 'text', ]
