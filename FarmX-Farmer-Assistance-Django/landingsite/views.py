from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    return render(request, 'landingsite/index.html')


@login_required
def bazaar(request):
    return render(request, 'landingsite/Bazaar-Home.html')
