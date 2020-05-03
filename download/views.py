from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View

from .utils import render_to_pdf
import datetime
from core.models import Basic_info, Education, Experience, Interest, Skills
from django.template.loader import get_template


class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        template = get_template('core/preview.html')
        context = {'user': request.user,
                   'basic_info': Basic_info.objects.get(user=request.user),
                   'education': Education.objects.get(user=request.user),
                   'experience': Experience.objects.get(user=request.user),
                   'skills': Skills.objects.get(user=request.user),
                   'interest': Interest.objects.get(user=request.user)
                   }
        html = template.render(context)
        pdf = render_to_pdf('core/preview.html', context)
        return pdf
