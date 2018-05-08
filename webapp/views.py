from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.http import Http404

from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm, SearchtimeForm

# Create your views here.
def index(request):
	pos = Post.objects.all()
	query = request.GET.get('q')
	if query:
		pos = pos.filter(
			Q(title__icontains=query) |
			Q(content__icontains=query)
			)

	context = {
		'pos':pos,
		'query':query
	}
	return render(request, 'index.html', context)

def detailpost(request, slug):
	instance = get_object_or_404(Post, slug=slug)
	return render(request, 'detailpost.html', {'instance':instance})

@login_required
def addpost(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			image = form.cleaned_data['image']
			post = form.save(commit=False)
			post.created_by = request.user
			post.save()

		return redirect('/')
	else:
		form = PostForm()
	return render(request, 'addpost.html', {'form':form})



def searchtime(request):
	pos = Post.objects.all()
	query = request.GET.get('q')
	if query:
		pos = pos.filter(created__range=query)

	context = {
		'pos':pos,
		'query':query,
	}
	return render(request, 'search.html', context)
