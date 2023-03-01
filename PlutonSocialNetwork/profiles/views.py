from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView


class UserLoginView(TemplateView):

    template_name = 'profiles/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({

        })
        return context


class AboutPageView(TemplateView):

    template_name = 'profiles/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({

        })
        return context


class DevPageView(TemplateView):

    template_name = 'profiles/dev.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({

        })