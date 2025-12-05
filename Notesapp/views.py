from django.shortcuts import render, redirect, get_object_or_404
from .models import Note

# Create your views here.
def index(request):
    newts = Note.objects.all()

    context = {
        'newts':newts,
    }

    return render(request, 'index.html', context)

def create_newt(request):
    if request.method == 'POST':
        new_newt = Note(
            title = request.POST.get('title'),
            content = request.POST.get('content')
        )
        new_newt.save()

    return redirect('/')

def update_newt(request, pk):
    newts = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        newts.title = request.POST.get('title')
        newts.content = request.POST.get('content')

        newts.save()


    return redirect('/', pk=newts.pk)

def delete_newt(request, pk):
    newts = get_object_or_404(Note, pk=pk)
    newts.delete()

    return redirect('/')

def toggle_pin(request, pk):
    newts = get_object_or_404(Note, pk=pk)
    newts.is_pinned = not newts.is_pinned
    newts.save()

    return redirect('/')

def search(request):
    newts = Note.objects.all()
    if request.method == 'POST':
        searchword = request.POST.get('searchword')

        result = Note.objects.filter(title__icontains = searchword)
        print(result)
    else:
        pass


    return render(request, 'index.html', {'result':result})

