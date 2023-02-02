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
    
def records(request, email):
    response = "You're looking at the assets assigned to email%s."
    return HttpResponse(response % email)

def assign(request, asset_id):
    asset_name = get_object_or_404(Asset, pk=asset_id)
    try:
        assign_asset = asset.assign_set.get(pk=request.POST['assigned_to'])
    except (KeyError, Record.DoesNotExist):
        #Redisplay the asset assign form.
        return render(request, 'assets/detail.html', {
            'asset': asset_name,
            'error_message': "You didn't select an asset"
        })
    else:
        assign_asset += 1
        assign_asset.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('dashboard:records', args=(asset_id,)))

def records(request, assigned_to):
    asset_assigned_to = get_object_or_404(Record, pk=assigned_to)
    return render(request, 'assets/records.html',{asset_assigned_to:'assigned_to'})


class IndexView(generic.ListView):
    template_name = 'assets/detail.html'
    context_object_name='latest_asset_list'

    def get_queryset(self):
        """Return the latest five added assets(not including those set to be added in the future)."""
        return Asset.objects.filter(date_added__lte=timezone.now()).order_by('-date_added')[:5]

class AssetView(generic.DetailView):
    model = Asset
    template_name = 'assets/detail.html'

    def get_queryset(self):
        """Excludes any assets that are assigned Already """
        return Asset.objects.filter(status__='a')

class RecordView(generic.DetailView):
    model = Record
    template_name = 'assets/records.html'