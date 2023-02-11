from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import Permission
from users.models import User
from assets.models import Asset
from records.models import Record
from django.views import generic
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.utils import timezone


def index(request):
    latest_asset_list = Asset.objects.order_by('-date_added')[:5]
    template = loader.get_template('assets/index.html')
    context = {'latest_asset_list': latest_asset_list,}
    return  HttpResponse(template.render(context, request))

def asset(request, asset_id):
    models = Asset.objects.all()
    return render(request, 'detail.html',{'models': models})
    