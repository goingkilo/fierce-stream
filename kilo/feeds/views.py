from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext,loader


def kpaper(request):
    return render( request, 'kpaper_typ.html', {'nothing':'nothing'})


