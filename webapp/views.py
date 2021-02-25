from django.shortcuts import render

# Create your views here.

def index_view(request):
    modern = Modern.objects.all()
    return render(request, 'index.html', context={'modern': modern}) 
