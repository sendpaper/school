from datetime import date, datetime, timedelta
from django.shortcuts import get_object_or_404, render

import events
from .models import LostItem, FoundItem

# Create your views here.

def index(request):
    #any code really bro

    all_lostitems = LostItem.objects.all().order_by('date')
    all_founditems = FoundItem.objects.all().order_by('date')

    lostitems_today = all_lostitems.filter(date = datetime.now())
    founditems_today = all_founditems.filter(date = datetime.now())


    context = {'all_lostitems':all_lostitems, 'all_founditems':all_founditems, 'lostitems_today':lostitems_today, 'founditems_today':founditems_today}

    return render(request, 'events/index.html', context)


def detail(request, lostitem_id):

    lostitem = get_object_or_404(LostItem, pk=lostitem_id)

    context = {'lostitem':lostitem}

    return render(request, 'events/detail.html', context)


def detail_2(request, founditem_id):

    founditem = get_object_or_404(FoundItem, pk=founditem_id) 

    context = {'founditem':founditem}

    return render(request, 'events/detail_2.html', context)


def search(request):

    all_lostitems = LostItem.objects.all().order_by('date')
    all_founditems = FoundItem.objects.all().order_by('date')

    if len(request.GET) == 0:
        relevant_lostitems = all_lostitems
        relevant_founditems = all_founditems
    else:
        search_string = request.GET['q']
        relevant_lostitems = all_lostitems.filter(title__contains = search_string)
        relevant_founditems = all_founditems.filter(title__contains = search_string)
    

    context = {'relevant_lostitems':relevant_lostitems, 'relevant_founditems':relevant_founditems}

    return render(request, 'events/search.html', context)