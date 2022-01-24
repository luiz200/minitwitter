from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from .models import public
from .forms import publicForm, CaptchaForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q


@login_required
def index(request):
    search = request.GET.get('search')
    user = request.user
    if search:
        publics = public.objects.filter(title__icontains=search )
    else:    
        publics_list = public.objects.all().order_by('-id')
        paginator = Paginator(publics_list, 10)
        page = request.GET.get('page')
        publics = paginator.get_page(page)
    
    return render(request, 'home/index.html', {'publics': publics})

@login_required
def newPost(request):
    if request.method == 'POST':
        form = publicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = publicForm()
        return render(request, 'home/newPost.html', {'form': form})