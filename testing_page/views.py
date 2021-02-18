from django.shortcuts import redirect
from django.views.generic import ListView
from .models import Question
from user.models import User
from django.contrib.auth.mixins import LoginRequiredMixin


class TestView(LoginRequiredMixin, ListView):
    model = Question
    paginate_by = 1
    login_url = 'login_url'

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset

    def post(self, request):
        user = User.objects.get(username=request.user.username)
        user.status = request.POST['status']
        user.save()
        return redirect('list_article_url')