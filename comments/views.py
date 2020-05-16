from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CommentForm
from .models import Comment


class CommentsView(TemplateView):
    template_name = 'temp/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CommentsView, self).get_context_data(*args, **kwargs)
        comments = Comment.objects.filter(available=True)
        context['comments'] = comments
        return context




class CommentCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView ):
    model = Comment
    template_name = 'temp/createcomments.html'
    form_class = CommentForm
    success_message = "Thank you for feedback, your comment is pending for approval."

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CommentCreateView, self).form_valid(form)
