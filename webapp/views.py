from django.shortcuts import render, redirect
from webapp.models import Modern
from django.http import HttpResponseRedirect, HttpResponseNotFound, Http404
from django.core.exceptions import ObjectDoesNotExist



# Create your views here.

def index_view(request):
    moderns = Modern.objects.all()
    return render(request, 'index.html', context={'moderns': moderns})

def modern_view(request, pk):
    try:
        modern = Modern.objects.get(pk=pk)
    except Modern.DoesNotExist:
        raise Http404
    return render(request, 'modern_view.html', context={'modern': modern})

def modern_create_view(request, *args, **kwargs):
    if request.method == "GET":
        return render(request, 'modern_create.html')
    elif request.method == "POST":
        title = request.POST.get("title")
        status = request.POST.get("status")
        time = request.POST.get("time")
        text_f = request.POST.get("text_f")
        if not time:
            time = None
        if not text_f:
            text_f = None

        modern = Modern.objects.create(
            title=title,
            status=status,
            time=time,
            text_f=text_f
        )

    return redirect('view', pk=modern.pk)

def modern_update_view(request, pk):
    modern = Modern.objects.all(pk=pk)
    if request.method == 'GET':
        return render(request, 'update.html', context={'modern': modern})
    elif request.method == 'POST':
        modern.title = request.POST.get('title')
        modern.text_f = request.POST.get('text_f')
        modern.time = request.POST.get('time')
        modern.text_f = request.POST.get('text_f')
        modern.save()
        return redirect('modern_view', pk=modern.pk)

