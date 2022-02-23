from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.views.generic.edit import CreateView
from django.views.generic import DetailView, ListView

from app.models import PasteBinModel


class CreatePasteBinView(CreateView, SuccessMessageMixin):
    model = PasteBinModel
    fields = ['title', 'slug', 'content']
    template_name = "index.html"
    success_message = "<a href='/%(id)s'>Here is the link</a>"
    success_url = '/'

class PasteBinView(DetailView):
    model = PasteBinModel
    template_name = "paste.html"
    context_object_name = "pastebin"


class AllPasteBinView(ListView):
    model = PasteBinModel
    template_name = "all.html"
