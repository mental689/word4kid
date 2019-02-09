from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from playground.models import *
import logging
logger = logging.getLogger(__name__)

# Create your views here.


class PlayView(LoginRequiredMixin, View):
    template_name = 'game.html'

    def get(self, request, *args, **kwargs):
        id = request.GET.get('id', None)
        v = Video.objects.filter(pk=id).first()
        context = {}
        if v is not None:
            context['video'] = v
            context['words'] = list(set([s.label.text for s in v.segments.all()]))
        return render(request, template_name=self.template_name, context=context)


