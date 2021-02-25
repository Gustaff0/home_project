from django.shortcuts import render

# Create your views here.

def index_view(request):
    modern = Modern.objects.all()
    return render(request, 'index.html', context={'modern': modern})

def modern_view(request):
    modern_id = request.GET.get('id')
    modern = Modern.objects.get(id=modern_id)
    return render(request, 'article_view.html', context={'modern': modern})

def modern_create_view(request):
    if request.method == "GET":
        return render(request, 'modern_create.html')
    elif request.method == "POST":
        title = request.POST.get("title")
        status = request.POST.get("status")
        time = request.POST.get("time")

        modern = Modern.objects.create(
            title=title,
            status=status,
            time=time
        )

        return render(request, 'modern_view.html', context={'modern': modern})

