from django.views.generic.base import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

class ReviewView(TemplateView):
    template_name = 'review.html'
