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
        return render(request, template_name=self.template_name, context={})


