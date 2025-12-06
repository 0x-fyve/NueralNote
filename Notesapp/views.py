from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from datetime import datetime, timedelta
from django.utils import timezone

# Create your views here.
def index(request):
    current_session_id = request.session.session_key

    newts = Note.objects.filter(owner_session_id=current_session_id)
    streak_number = request.session.get('streak_count', 0)

    context = {
        'newts':newts,
        'streak_number':streak_number
    }

    return render(request, 'index.html', context)

def create_newt(request):
    if request.method == 'POST':
        if not request.session.session_key:
            request.session.create()

        current_session_id = request.session.session_key    

        new_newt = Note(
            title = request.POST.get('title'),
            content = request.POST.get('content'),
            owner_session_id = current_session_id
        )
        new_newt.save()

        
        today_str = timezone.now().date().strftime('%Y-%m-%d')
        
        last_posted = request.session.get('last_posted_date')
        current_streak = request.session.get('streak_count', 0)

        if last_posted == today_str:
            
            pass
        
        elif last_posted:

            last_date_obj = datetime.strptime(last_posted, '%Y-%m-%d').date()
            yesterday_obj = timezone.now().date() - timedelta(days=1)

            if last_date_obj == yesterday_obj:
                
                request.session['streak_count'] = current_streak + 1
            else:
                
                request.session['streak_count'] = 0
        else:
            
            request.session['streak_count'] = 1

        request.session['last_posted_date'] = today_str
        

        return redirect('/')

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

