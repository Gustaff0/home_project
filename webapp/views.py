from django.shortcuts import render
from webapp.models import Modern

# Create your views here.

def index_view(request):
    moderns = Modern.objects.all()
    return render(request, 'index.html', context={'moderns': moderns})

def modern_view(request):
    modern_id = request.GET.get('id')
    modern = Modern.objects.get(id=modern_id)
    return render(request, 'modern_view.html', context={'modern': modern})

def modern_create_view(request):
    if request.method == "GET":
        return render(request, 'modern_create.html')
    elif request.method == "POST":
        title = request.POST.get("title")
        status = request.POST.get("status")
        time = request.POST.get("time")
        if not time:
            time = None

        modern = Modern.objects.create(
            title=title,
            status=status,
            time=time
        )

        return render(request, 'modern_view.html', context={'modern': modern})

