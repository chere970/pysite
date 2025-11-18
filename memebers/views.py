from django.shortcuts import render
from .models import Member
from django.template import loader
from django.http import HttpResponse
# Create your views here.


def testing(requiest):
    members = Member.objects.all()
    template = loader.get_template('template.html')
    context = {
        'mymembers': members,
    }
    return HttpResponse(template.render(context, requiest))
