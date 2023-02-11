from django.shortcuts import render

# Create your views here.

from users.models import User
from assets.models import Asset
from records.models import Record
from django.views import generic
from django.http import Http404

def index(request):
    """View function for home page of site"""

    #Generate counts for some of the main objects
    num_users = User.objects.all().count()
    num_assets = Asset.objects.all().count()

    #Available assets(status = 'a')
    #num_assets_available = Asset.objects.filter(status_exact='a').count()
    
    context = {
        'num_users': num_users,
        'num_assets': num_assets,
        #'num_assets_available': num_assets_available,

    }
    
    # Render the HTML template index.html with the data in the context above
    return render(request, 'index.html', context=context)

def AssetListView(request,):
    records = Record.objects.all()
    return render(request, 'home.html', {'records':records})